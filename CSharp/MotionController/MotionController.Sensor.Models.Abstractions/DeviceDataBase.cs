using Newtonsoft.Json;

namespace MotionController.Sensor.Models;

public class DeviceDataBase : ISessionIdentifier
{
    [JsonProperty("sessionId")]
    public Guid SessionId { get; set; }

    [JsonProperty("timestamp")]
    public DateTime Timestamp { get; set; }
}
