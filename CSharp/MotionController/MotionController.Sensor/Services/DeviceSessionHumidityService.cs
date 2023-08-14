using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionHumidityService : IService
{
    Task<bool> AddDeviceSessionEnvironmentAsync(DeviceSessionHumidity deviceSessionHumidity);
}

internal class DeviceSessionHumidityService : ServiceBase<DeviceSessionHumidityService>, IDeviceSessionHumidityService
{
    public DeviceSessionHumidityService(ILogger<DeviceSessionHumidityService> logger, IDeviceSessionHumidityRepository deviceSessionHumidityRepository)
        : base(logger)
    {
        DeviceSessionHumidityRepository = deviceSessionHumidityRepository;
    }

    private IDeviceSessionHumidityRepository DeviceSessionHumidityRepository { get; }

    public async Task<bool> AddDeviceSessionEnvironmentAsync(DeviceSessionHumidity deviceSessionHumidity)
    {
        return await DeviceSessionHumidityRepository.AddAsync(deviceSessionHumidity);
    }
}
