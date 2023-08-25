using Autofac;
using MQTTnet;
using MQTTnet.Client;

namespace MotionController.Extensions.DependencyInjection;

public static class ContainerBuilderExtensions
{
    public static ContainerBuilder RegisterMQTT(this ContainerBuilder containerBuilder)
    {
        containerBuilder.RegisterType<MqttFactory>()
            .AsSelf()
            .SingleInstance();

        return containerBuilder;
    }

    public static ContainerBuilder RegisterMQTTClient(this ContainerBuilder containerBuilder)
    {
        containerBuilder.Register((cc, p) =>
        {
            var mqttFactory = cc.Resolve<MqttFactory>();

            return mqttFactory.CreateMqttClient();
        })
            .As<IMqttClient>()
            .SingleInstance();

        return containerBuilder;
    }
}
