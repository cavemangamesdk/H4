using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;

namespace MotionController.Services;

public interface IDeviceSessionGyroscopeService : IService
{
    Task<bool> AddDeviceSessionGyroscopeAsync(DeviceSessionGyroscope deviceSessionGyroscope);
}

internal class DeviceSessionGyroscopeService : ServiceBase<DeviceSessionGyroscopeService>, IDeviceSessionGyroscopeService
{
    public DeviceSessionGyroscopeService(ILogger<DeviceSessionGyroscopeService> logger, IDeviceSessionGyroscopeRepository deviceSessionGyroscopeRepository)
        : base(logger)
    {
        DeviceSessionGyroscopeRepository = deviceSessionGyroscopeRepository;
    }

    private IDeviceSessionGyroscopeRepository DeviceSessionGyroscopeRepository { get; }

    public async Task<bool> AddDeviceSessionGyroscopeAsync(DeviceSessionGyroscope deviceSessionGyroscope)
    {
        return await DeviceSessionGyroscopeRepository.AddAsync(deviceSessionGyroscope);
    }
}
