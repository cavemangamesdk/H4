using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.Extensions.Hosting;
using MotionController.MQTT.Client.Subscriber;
using MotionController.Sensor.Messaging;
using System.Text;

namespace MotionController.BackgroundServices;

public interface IMQTTClientBackgroundService : IBackgroundService
{
}

internal class MQTTClientBackgroundService : BackgroundService<MQTTClientBackgroundService>, IMQTTClientBackgroundService
{
    public MQTTClientBackgroundService(ILogger<MQTTClientBackgroundService> logger, IMessageHandlerResolver messageHandlerResolver, IServiceProvider serviceProvider, IMQTTSubscriberClientFactory mqttSubscriberClientFactory)
        : base(logger)
    {
        MessageHandlerResolver = messageHandlerResolver;
        ServiceProvider = serviceProvider;
        MqttSubscriberClientFactory = mqttSubscriberClientFactory;
    }

    private IMessageHandlerResolver MessageHandlerResolver { get; }
    private IServiceProvider ServiceProvider { get; }
    private IMQTTSubscriberClientFactory MqttSubscriberClientFactory { get; }

    protected override async Task ExecuteLogicAsync(CancellationToken cancellationToken)
    {
        try
        {
            using var subscriberClient = MqttSubscriberClientFactory.CreateSubscriberClient();

            subscriberClient.ReceivedMessageAsync += OnReceivedMessageAsync;

            await subscriberClient.SubscribeAsync("sensehat/#", MQTTnet.Protocol.MqttQualityOfServiceLevel.ExactlyOnce, cancellationToken);
        }
        catch (Exception ex)
        {
            Logger.LogError(ex, ex.Message);
            throw;
        }
    }

    private async Task OnReceivedMessageAsync(ArraySegment<byte> payload, string topic)
    {
        try
        {
            using var scope = ServiceProvider.CreateScope();

            var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

            var utf8Message = Encoding.UTF8.GetString(payload);

            var messageHandler = MessageHandlerResolver.Resolve(topic);
            if (messageHandler == default)
            {
                Logger.LogWarning($"No message handler for the given topic {topic}");
                return;
            }

            await messageHandler.HandleAsync(utf8Message);

            unitOfWork.Complete();
        }
        catch (Exception ex)
        {
            Logger.LogError(ex, ex.Message);
            throw;
        }
    }
}
