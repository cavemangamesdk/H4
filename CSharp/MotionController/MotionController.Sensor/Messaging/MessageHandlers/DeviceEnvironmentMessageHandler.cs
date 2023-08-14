using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.BackgroundServices;
using MotionController.Data;
using MotionController.MQTT;
using MotionController.MQTT.Messages;
using MotionController.Sensor.Models;
using MotionController.Services;
using Newtonsoft.Json;

namespace MotionController.Sensor.Messaging.MessageHandlers
{
    class DeviceEnvironment : ISessionIdentifier
    {
        [JsonProperty("sessionId")]
        public Guid SessionId { get; set; }

        [JsonProperty("temperature")]
        public float Temperature { get; set; }

        [JsonProperty("temperatureFromHumidity")]
        public float TemperatureFromHumidity { get; set; }

        [JsonProperty("temperatureFromPressure")]
        public float TemperatureFromPressure { get; set; }

        [JsonProperty("humidity")]
        public float Humidity { get; set; }

        [JsonProperty("pressure")]
        public float Pressure { get; set; }

        [JsonProperty("timestamp")]
        public DateTime Timestamp { get; set; }
    }

    [MQTTTopic("encyclopedia/environment")]
    internal class DeviceEnvironmentMessageHandler : MessageHandlerBase<DeviceEnvironment>
    {
        public DeviceEnvironmentMessageHandler(ILogger<DeviceEnvironmentMessageHandler> logger, IServiceProvider serviceProvider)
            : base(serviceProvider)
        {
            Logger = logger;
        }

        private ILogger<DeviceEnvironmentMessageHandler> Logger { get; }

        protected override async Task HandleModelAsync(DeviceEnvironment model)
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
                TemperatureCelsius = model.Temperature,
                TemperatureFromHumidityCelsius = model.TemperatureFromHumidity,
                TemperatureFromPressureCelsius = model.TemperatureFromPressure,
                HumidityPercentage = model.Humidity,
                PressureMillibars = model.Pressure,
                Timestamp = model.Timestamp
            };
            await deviceSessionEnvironmentService.AddDeviceSessionEnvironmentAsync(dbDeviceSessionEnvironment);

            unitOfWork.Complete();
        }
    }
}
