using Newtonsoft.Json;

namespace MotionController.Sensor.Models;

public sealed class DeviceEnvironmentDataBase
{
    [JsonProperty("humidity_sensor")]
    public DeviceHumidityDataBase? HumiditySensor { get; set; }

    [JsonProperty("pressure_sensor")]
    public DevicePressureDataBase? PressureSensor { get; set; }
}

public sealed class DeviceEnvironmentData : DeviceDataBase
{
    [JsonProperty("data")]
    public DeviceEnvironmentDataBase? Data { get; set; }
}