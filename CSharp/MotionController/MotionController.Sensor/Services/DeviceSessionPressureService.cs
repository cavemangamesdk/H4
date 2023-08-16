using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Models;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionPressureService : IService
{
    Task<IEnumerable<DeviceSessionPressure?>> GetDeviceSessionPressuresAsync(DeviceSession deviceSession);
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

    public Task<IEnumerable<DeviceSessionPressure?>> GetDeviceSessionPressuresAsync(DeviceSession deviceSession)
    {
        return DeviceSessionPressureRepository.GetAsync(deviceSession.Id);
    }

    public async Task<bool> AddDeviceSessionPressureAsync(DeviceSessionPressure deviceSessionPressure)
    {
        return await DeviceSessionPressureRepository.AddAsync(deviceSessionPressure);
    }
}
