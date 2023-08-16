using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionPressureService : IService
{
    Task<bool> AddDeviceSessionPressureAsync(DeviceSessionPressure deviceSessionPressure);
}

internal class DeviceSessionPressureService : ServiceBase<DeviceSessionPressureService>, IDeviceSessionPressureService
{
    public DeviceSessionPressureService(ILogger<DeviceSessionPressureService> logger, IDeviceSessionPressureRepository deviceSessionPressureRepository)
        : base(logger)
    {
        DeviceSessionPressureRepository = deviceSessionPressureRepository;
    }

    public IDeviceSessionPressureRepository DeviceSessionPressureRepository { get; }

    public async Task<bool> AddDeviceSessionPressureAsync(DeviceSessionPressure deviceSessionPressure)
    {
        return await DeviceSessionPressureRepository.AddAsync(deviceSessionPressure);
    }
}
