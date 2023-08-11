using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.Db.Data.Models;
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

public interface ISessionIdentifier
{
    Guid SessionId { get; set; }
}

class Device : ISessionIdentifier
{
    public Guid SessionId { get; set; }
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
        MqttClient = CreateAndConnectMQTTClientAsync();
    }

    private IServiceProvider ServiceProvider { get; }
    private IMqttClient MqttClient { get; set; }

    protected override async Task ExecuteLogicAsync(CancellationToken cancellationToken)
    {
        try
        {
            s_Map.TryAdd("encyclopedia/environment", typeof(DeviceEnv));

            if (!MqttClient.IsConnected)
            {
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

                var response = await MqttClient.ConnectAsync(options, cancellationToken);
                if (!response.ResultCode.Equals(MqttClientConnectResultCode.Success))
                {
                    throw new SystemException();
                }

                MqttClient.ApplicationMessageReceivedAsync += OnApplicationMessageReceivedFuncAsync;

                await MqttClient.SubscribeAsync("encyclopedia/#", MQTTnet.Protocol.MqttQualityOfServiceLevel.ExactlyOnce, cancellationToken);
            }

            while (cancellationToken.IsCancellationRequested)
            {
            }

            //var disconnectOptions = new MqttClientDisconnectOptions
            //{
            //    Reason = MqttClientDisconnectOptionsReason.NormalDisconnection,
            //    ReasonString = "Disconnect"
            //};

            //await MqttClient.DisconnectAsync(disconnectOptions);

            //MqttClient?.Dispose();
        }
        catch (Exception ex)
        {
            Logger.LogError(ex, ex.Message);
            throw;
        }
    }

    private static IMqttClient CreateAndConnectMQTTClientAsync()
    {
        var factory = new MqttFactory();

        var client = factory.CreateMqttClient();

        return client;
    }

    private async Task OnApplicationMessageReceivedFuncAsync(MqttApplicationMessageReceivedEventArgs eventArgs)
    {
        var utf8Message = Encoding.UTF8.GetString(eventArgs.ApplicationMessage.PayloadSegment);

        Logger.LogInformation(utf8Message);

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
            await HandleDeviceEnvAsync(deviceSession, deviceEnviroment);
        }

        unitOfWork.Complete();
    }

    private async Task HandleDeviceEnvAsync(DeviceSession? deviceSession, DeviceEnv deviceEnviroment)
    {
        // TODO: Add Throw.IfNull();
        if(deviceSession?.Equals(default) ?? true)
        {
            return;
        }

        using var scope = ServiceProvider.CreateScope();

        var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

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

        unitOfWork.Complete();
    }
}
