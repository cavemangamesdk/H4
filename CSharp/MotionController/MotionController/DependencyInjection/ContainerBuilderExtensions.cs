using Autofac;
using MotionController.BackgroundServices;
using MotionController.Extensions.Autofac;

namespace MotionController.Extensions.DependencyInjection;

public static class ContainerBuilderExtensions
{
    public static ContainerBuilder RegisterMotionController(this ContainerBuilder containerBuilder)
    {
        return containerBuilder;
    }

    public static ContainerBuilder WithMQTTClientBackgroundService(this ContainerBuilder containerBuilder)
    {
        return containerBuilder.RegisterBackgroundService<MQTTClientBackgroundService>();
    }
}
