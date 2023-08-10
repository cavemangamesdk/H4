using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.Extensions.Hosting;
using MotionController.Services;
using MQTTnet;
using MQTTnet.Client;
using Newtonsoft.Json;
using System;
using System.Collections.Concurrent;
using System.Text;

namespace MotionController.BackgroundServices;

public interface IMQTTClientBackgroundService : IBackgroundService
{
}

class Device : ISessionIdentifier
{
    public Guid SessionId { get; set; }
}

public interface ISessionIdentifier
{
    Guid SessionId { get; set; }
}

class DeviceEnv : ISessionIdentifier
{
    [JsonProperty("sessionId")]
    public Guid SessionId { get; set; }

    [JsonProperty("temperature")]
    public float Temperature { get; set; }

    [JsonProperty("humidity")]
    public float Humidity { get; set; }

    [JsonProperty("pressure")]
    public float Pressure { get; set; }

    [JsonProperty("timestamp")]
    public DateTime Timestamp { get; set; }
}

internal class MQTTClientBackgroundService : BackgroundService<MQTTClientBackgroundService>, IMQTTClientBackgroundService
{
    private readonly ConcurrentDictionary<string, Type> s_Map = new();

    public MQTTClientBackgroundService(ILogger<MQTTClientBackgroundService> logger, IServiceProvider serviceProvider)
        : base(logger)
    {
        ServiceProvider = serviceProvider;
    }

    private IServiceProvider ServiceProvider { get; }

    protected override async Task ExecuteLogicAsync(CancellationToken cancellationToken)
    {
        try
        {
            s_Map.TryAdd("encyclopedia/environment", typeof(DeviceEnv));

            var client = await CreateAndConnectMQTTClientAsync();

            client.ApplicationMessageReceivedAsync += OnApplicationMessageReceivedFuncAsync;

            await client.SubscribeAsync("encyclopedia/#", MQTTnet.Protocol.MqttQualityOfServiceLevel.ExactlyOnce, cancellationToken);

            while (cancellationToken.IsCancellationRequested)
            {
            }
        }
        catch (Exception ex)
        {
            Logger.LogError(ex, ex.Message);
            throw;
        }
    }

    private static async Task<IMqttClient> CreateAndConnectMQTTClientAsync()
    {
        var factory = new MqttFactory();

        var client = factory.CreateMqttClient();

        MqttClientOptionsBuilderTlsParameters tlsOptions = new()
        {
            SslProtocol = System.Security.Authentication.SslProtocols.Tls12,
            UseTls = true,
            AllowUntrustedCertificates = true
        };

        var options = new MqttClientOptionsBuilder()
            .WithTcpServer("3c6ea0ec32f6404db6fd0439b0d000ce.s2.eu.hivemq.cloud", 8883)
            .WithCredentials("mvp2023", "wzq6h2hm%WLaMh$KYXj5")
            .WithClientId(Guid.NewGuid().ToString())
            .WithTls(tlsOptions)
            .WithProtocolVersion(MQTTnet.Formatter.MqttProtocolVersion.V500)
            .Build();

        var response = await client.ConnectAsync(options);
        if (!response.ResultCode.Equals(MqttClientConnectResultCode.Success))
        {
            throw new SystemException();
        }

        return client;
    }

    private async Task OnApplicationMessageReceivedFuncAsync(MqttApplicationMessageReceivedEventArgs eventArgs)
    {
        var utf8Message = Encoding.UTF8.GetString(eventArgs.ApplicationMessage.PayloadSegment);

        if (!s_Map.TryGetValue(eventArgs.ApplicationMessage.Topic, out var modelType))
        {
            Logger.LogError($"Unsupported model type for given topic {eventArgs.ApplicationMessage.Topic}");
            return;
        }

        var model = (ISessionIdentifier?)JsonConvert.DeserializeObject(utf8Message, modelType);
        if (model == default)
        {
            return;
        }

        await HandleModelAsync(model);
    }

    private async Task HandleModelAsync(ISessionIdentifier? model)
    {
        // TODO: Add Throw.IfNull();

        using var scope = ServiceProvider.CreateScope();

        var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

        var deviceSessionService = scope.ServiceProvider.GetRequiredService<IDeviceSessionService>();

        var deviceSession = await deviceSessionService.GetOrAddDeviceSessionAsync(model!.SessionId);
        if (deviceSession?.Equals(default) ?? true)
        {
            Logger.LogError("Bullshit");
            throw new Exception("Bullshit");
        }

        if (model is DeviceEnv deviceEnviroment)
        {
            Logger.LogInformation($"Received payload from Session Id {deviceSession.SessionId} (${deviceEnviroment.Timestamp})");

            var deviceSessionEnvironmentService = scope.ServiceProvider.GetRequiredService<IDeviceSessionEnvironmentService>();

            var dbDeviceSessionEnvironment = new Db.Data.Models.DeviceSessionEnvironment
            {
                SessionId = deviceSession.SessionId,
                TemperatureCelsius = deviceEnviroment.Temperature,
                HumidityPercentage = deviceEnviroment.Humidity,
                PressureMillibars = deviceEnviroment.Pressure,
                Timestamp = deviceEnviroment.Timestamp
            };
            await deviceSessionEnvironmentService.AddDeviceSessionEnvironmentAsync(dbDeviceSessionEnvironment);
        }

        unitOfWork.Complete();
    }
}
