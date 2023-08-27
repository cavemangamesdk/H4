using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;

namespace MotionController.MQTT.Client.Subscriber;

public interface IMQTTSubscriberClientFactory
{
    IMQTTSubscriberClient CreateSubscriberClient();
}

internal sealed class MQTTSubscriberClientFactory : IMQTTSubscriberClientFactory
{
    public MQTTSubscriberClientFactory(IServiceProvider serviceProvider)
    {
        ServiceProvider = serviceProvider;
    }

    private IServiceProvider ServiceProvider { get; }

    public IMQTTSubscriberClient CreateSubscriberClient()
    {
        var logger = ServiceProvider.GetRequiredService<ILogger<MQTTSubscriberClient>>();
        var mqttClient = ServiceProvider.GetRequiredService<MQTTnet.Client.IMqttClient>();
        var mqttClientOptions = ServiceProvider.GetRequiredService<MQTTnet.Client.MqttClientOptions>();

        return new MQTTSubscriberClient(logger, mqttClient, mqttClientOptions);
    }
}