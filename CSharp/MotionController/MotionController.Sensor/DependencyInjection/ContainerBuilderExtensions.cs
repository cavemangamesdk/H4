using Autofac;
using MotionController.BackgroundServices;
using MotionController.Db.Data.Providers;
using MotionController.DependencyInjection;
using MotionController.Extensions.Autofac;
using MotionController.MQTT;
using MotionController.MQTT.Messages;
using MotionController.Sensor.Messaging;
using System.Reflection;

namespace MotionController.Extensions.DependencyInjection;

public static class ContainerBuilderExtensions
{
    public static ContainerBuilder RegisterMotionController(this ContainerBuilder containerBuilder, MotionOptions? motionOptions)
    {
        if (motionOptions == null)
        {
            throw new Exception("");
        }

        containerBuilder.RegisterAssemblyMessageHandlers(typeof(MotionOptions).Assembly);

        containerBuilder.RegisterType<MessageHandlerResolver>()
            .As<IMessageHandlerResolver>()
            .InstancePerLifetimeScope();

        containerBuilder.RegisterSqlClientProvider<MotionProvider>(motionOptions.SqlClientProviderSettings);

        containerBuilder.RegisterModule<ServiceModule<MotionOptions>>();

        return containerBuilder;
    }

    public static ContainerBuilder WithMQTTClientBackgroundService(this ContainerBuilder containerBuilder)
    {
        return containerBuilder.RegisterBackgroundService<MQTTClientBackgroundService>();
    }

    private static ContainerBuilder RegisterAssemblyMessageHandlers(this ContainerBuilder containerBuilder, Assembly assembly)
    {
        var messageHandlers = assembly.GetTypes().Where(t => t.IsAssignableTo<IMessageHandler>() && t.GetCustomAttributes<MQTTTopicAttribute>().Any());
        foreach (var messageHandler in messageHandlers)
        {
            var attributes = messageHandler.GetCustomAttributes<MQTTTopicAttribute>();
            foreach (var attribute in attributes)
            {
                containerBuilder.RegisterType(messageHandler).Keyed<IMessageHandler>(attribute.Topic);
            }
        }

        return containerBuilder;
    }
}
