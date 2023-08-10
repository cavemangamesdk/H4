using Microsoft.Extensions.Logging;
using MotionController.Extensions.Hosting;
using MotionController.Services;
using MQTTnet;
using MQTTnet.Client;
using Newtonsoft.Json;
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

    public MQTTClientBackgroundService(ILogger<MQTTClientBackgroundService> logger, IDeviceSessionService deviceService)
        : base(logger)
    {
        DeviceSessionService = deviceService;
    }

    private IDeviceSessionService DeviceSessionService { get; }

    protected override async Task ExecuteLogicAsync(CancellationToken cancellationToken)
    {
        s_Map.TryAdd("encyclopedia/environment", typeof(DeviceEnv));

        var factory = new MqttFactory();

        var client = factory.CreateMqttClient();

        MqttClientOptionsBuilderTlsParameters tlsOptions = new MqttClientOptionsBuilderTlsParameters();
        tlsOptions.SslProtocol = System.Security.Authentication.SslProtocols.Tls12;
        tlsOptions.UseTls = true;
        tlsOptions.AllowUntrustedCertificates = true;

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

        client.ApplicationMessageReceivedAsync += OnApplicationMessageReceivedFuncAsync;

        await client.SubscribeAsync("encyclopedia/#", MQTTnet.Protocol.MqttQualityOfServiceLevel.AtLeastOnce, CancellationToken.None);

        while (client.IsConnected)
        {
            await client.PingAsync(CancellationToken.None);

            await Task.Delay(1000);
        }
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

        var deviceSession = await DeviceSessionService.GetOrAddDeviceSessionAsync(model.SessionId);
        if(deviceSession == default)
        {
            Logger.LogError("Bullshit");
            throw new Exception("Bullshit");
        }

        Logger.LogInformation($"Received payload from Session Id {deviceSession.SessionId}");
    }
}
