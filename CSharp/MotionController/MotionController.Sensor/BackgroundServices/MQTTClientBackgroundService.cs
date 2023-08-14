using Microsoft.Extensions.Logging;
using MotionController.Extensions.Hosting;
using MotionController.Sensor.Messaging;
using MotionController.Sensor.Models;
using MQTTnet;
using MQTTnet.Client;
using Newtonsoft.Json;
using System.Text;

namespace MotionController.BackgroundServices;

public interface IMQTTClientBackgroundService : IBackgroundService
{
}

internal class MQTTClientBackgroundService : BackgroundService<MQTTClientBackgroundService>, IMQTTClientBackgroundService
{
    public MQTTClientBackgroundService(ILogger<MQTTClientBackgroundService> logger, IMessageHandlerResolver messageHandlerResolver)
        : base(logger)
    {
        MessageHandlerResolver = messageHandlerResolver;
        MqttClient = CreateAndConnectMQTTClientAsync();
    }

    private IMessageHandlerResolver MessageHandlerResolver { get; }
    private IMqttClient MqttClient { get; set; }

    protected override async Task ExecuteLogicAsync(CancellationToken cancellationToken)
    {
        try
        {
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

                await MqttClient.SubscribeAsync("sensehat/#", MQTTnet.Protocol.MqttQualityOfServiceLevel.ExactlyOnce, cancellationToken);
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

        var messageHandler = MessageHandlerResolver.Resolve(eventArgs.ApplicationMessage.Topic);
        if (messageHandler == default)
        {
            Logger.LogWarning($"No message handler for the given topic {eventArgs.ApplicationMessage.Topic}");
            return;
        }

        await messageHandler.HandleAsync(utf8Message);
    }
}
