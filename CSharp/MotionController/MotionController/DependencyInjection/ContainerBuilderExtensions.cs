using Autofac;
using MotionController.BackgroundServices;
using MotionController.Db.Data.Providers;
using MotionController.DependencyInjection;
using MotionController.Extensions.Autofac;

namespace MotionController.Extensions.DependencyInjection;

public static class ContainerBuilderExtensions
{
    public static ContainerBuilder RegisterMotionController(this ContainerBuilder containerBuilder, MotionOptions? motionOptions)
    {
        if(motionOptions == null)
        {
            throw new Exception("");
        }

        containerBuilder.RegisterSqlClientProvider<MotionProvider>(motionOptions.SqlClientProviderSettings);

        containerBuilder.RegisterModule<ServiceModule<MotionOptions>>();

        return containerBuilder;
    }

    public static ContainerBuilder WithMQTTClientBackgroundService(this ContainerBuilder containerBuilder)
    {
        return containerBuilder.RegisterBackgroundService<MQTTClientBackgroundService>();
    }
}
