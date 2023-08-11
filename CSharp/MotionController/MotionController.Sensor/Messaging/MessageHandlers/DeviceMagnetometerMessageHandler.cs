using Microsoft.Extensions.Logging;
using MotionController.BackgroundServices;
using MotionController.MQTT;
using MotionController.MQTT.Messages;
using Newtonsoft.Json;

namespace MotionController.Sensor.Messaging.MessageHandlers
{
    class DeviceMagnetometer : ISessionIdentifier
    {
        [JsonProperty("sessionId")]
        public Guid SessionId { get; set; }

        [JsonProperty("north")]
        public float North { get; set; }

        [JsonProperty("x_raw")]
        public float XRaw { get; set; }

        [JsonProperty("y_raw")]
        public float YRaw { get; set; }

        [JsonProperty("z_raw")]
        public float ZRaw { get; set; }

        [JsonProperty("timestamp")]
        public DateTime Timestamp { get; set; }
    }

    [MQTTTopic("encyclopedia/magnetometer")]
    internal sealed class DeviceMagnetometerMessageHandler : MessageHandlerBase<DeviceMagnetometer>
    {
        public DeviceMagnetometerMessageHandler(ILogger<DeviceMagnetometerMessageHandler> logger, IServiceProvider serviceProvider)
            : base(serviceProvider)
        {
            Logger = logger;
        }

        private ILogger<DeviceMagnetometerMessageHandler> Logger { get; }

        protected override Task HandleModelAsync(DeviceMagnetometer model)
        {
            Logger.LogInformation("encyclopedia/magnetometer");
            return Task.CompletedTask;
        }
    }
}
