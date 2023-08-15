using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionGyroscopeService : IService
{
    Task<bool> AddDeviceSessionHumidityAsync(DeviceSessionGyroscope deviceSessionGyroscope);
}

internal class DeviceSessionGyroscopeService : ServiceBase<DeviceSessionGyroscopeService>, IDeviceSessionGyroscopeService
{
    public DeviceSessionGyroscopeService(ILogger<DeviceSessionGyroscopeService> logger, IDeviceSessionGyroscopeRepository deviceSessionGyroscopeRepository)
        : base(logger)
    {
        DeviceSessionGyroscopeRepository = deviceSessionGyroscopeRepository;
    }

    private IDeviceSessionGyroscopeRepository DeviceSessionGyroscopeRepository { get; }

    public async Task<bool> AddDeviceSessionHumidityAsync(DeviceSessionGyroscope deviceSessionGyroscope)
    {
        return await DeviceSessionGyroscopeRepository.AddAsync(deviceSessionGyroscope);
    }
}
