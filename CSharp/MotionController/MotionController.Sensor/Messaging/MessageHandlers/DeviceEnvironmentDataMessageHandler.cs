using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.MQTT;
using MotionController.MQTT.Messages;
using MotionController.Sensor.Models;
using MotionController.Services;

namespace MotionController.Sensor.Messaging.MessageHandlers
{
    [MQTTTopic("encyclopedia/environment")]
    internal class DeviceEnvironmentDataMessageHandler : MessageHandlerBase<DeviceEnvironmentData>
    {
        public DeviceEnvironmentDataMessageHandler(ILogger<DeviceEnvironmentDataMessageHandler> logger, IServiceProvider serviceProvider)
            : base(serviceProvider)
        {
            Logger = logger;
        }

        private ILogger<DeviceEnvironmentDataMessageHandler> Logger { get; }

        protected override async Task HandleModelAsync(DeviceEnvironmentData model)
        {
            using var scope = ServiceProvider.CreateScope();

            var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

            var deviceSessionEnvironmentService = scope.ServiceProvider.GetRequiredService<IDeviceSessionEnvironmentService>();

            var deviceSessionService = scope.ServiceProvider.GetRequiredService<IDeviceSessionService>();

            var deviceSession = await deviceSessionService.GetOrAddDeviceSessionAsync(model.SessionId);
            if (deviceSession?.Equals(default) ?? true)
            {
                Logger.LogError("Bullshit");
                throw new Exception("Bullshit");
            }

            var dbDeviceSessionEnvironment = new Db.Data.Models.DeviceSessionEnvironment
            {
                SessionId = deviceSession.SessionId,
                TemperatureCelsius = model?.Data?.HumiditySensor?.Temperature ?? default,
                TemperatureFromHumidityCelsius = model?.Data?.HumiditySensor?.Temperature ?? default,
                HumidityPercentage = model?.Data?.HumiditySensor?.Humidity ?? default,
                TemperatureFromPressureCelsius = model?.Data?.PressureSensor?.Temperature ?? default,
                PressureMillibars = model?.Data?.PressureSensor?.Pressure ?? default,
                Timestamp = model?.Timestamp ?? default
            };
            await deviceSessionEnvironmentService.AddDeviceSessionEnvironmentAsync(dbDeviceSessionEnvironment);

            unitOfWork.Complete();
        }
    }
}
