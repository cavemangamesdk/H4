using Microsoft.Extensions.Logging;
using MQTTnet.Client;

namespace MotionController.MQTT.Client.Subscriber;

public interface IMQTTSubscriberClient : IMQTTClient
{
    // TODO: Move topic and qualityOfServiceLevel into Client settings
    Task SubscribeAsync(string? topic, MQTTnet.Protocol.MqttQualityOfServiceLevel qualityOfServiceLevel, CancellationToken cancellationToken);
}

internal class MQTTSubscriberClient : MQTTClientBase, IMQTTSubscriberClient
{
    public MQTTSubscriberClient(ILogger<MQTTSubscriberClient> logger, IMqttClient mqttClient)
        : base(logger, mqttClient)
    {
    }

    public Func<ArraySegment<byte>, string, Task>? ReceivedMessageAsync { get; set; }

    public async Task SubscribeAsync(string? topic, MQTTnet.Protocol.MqttQualityOfServiceLevel qualityOfServiceLevel, CancellationToken cancellationToken)
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

            await MqttClient.SubscribeAsync(topic, qualityOfServiceLevel, cancellationToken).ConfigureAwait(false);
        }

        while (!cancellationToken.IsCancellationRequested && MqttClient.IsConnected)
        {
            cancellationToken.WaitHandle.WaitOne(10000);
        }

        if (!cancellationToken.IsCancellationRequested && !MqttClient.IsConnected)
        {
            throw new Exception("Mqtt Client not connected");
        }
    }

    private async Task OnApplicationMessageReceivedFuncAsync(MqttApplicationMessageReceivedEventArgs args)
    {
        try
        {
            if (!MqttClient.IsConnected)
            {
                throw new InvalidOperationException("Mqtt Client not connected.");
            }

            // TODO: fix possible null reference
            await ReceivedMessageAsync?.Invoke(args.ApplicationMessage.PayloadSegment, args.ApplicationMessage.Topic);
        }
        catch (Exception ex)
        {
            Logger.LogError(ex, ex.Message);
            throw;
        }
    }
}
