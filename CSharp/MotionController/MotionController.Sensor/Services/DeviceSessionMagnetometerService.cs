using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionMagnetometerService : IService
{
    Task<bool> AddDeviceSessionMagnetometerAsync(DeviceSessionMagnetometer deviceSessionMagnetometer);
}

internal class DeviceSessionMagnetometerService : ServiceBase<DeviceSessionMagnetometerService>, IDeviceSessionMagnetometerService
{
    public DeviceSessionMagnetometerService(ILogger<DeviceSessionMagnetometerService> logger, IDeviceSessionMagnetometerRepository deviceSessionMagnetometerRepository)
        : base(logger)
    {
        DeviceSessionMagnetometerRepository = deviceSessionMagnetometerRepository;
    }

    private IDeviceSessionMagnetometerRepository DeviceSessionMagnetometerRepository { get; }

    public async Task<bool> AddDeviceSessionMagnetometerAsync(DeviceSessionMagnetometer deviceSessionMagnetometer)
    {
        return await DeviceSessionMagnetometerRepository.AddAsync(deviceSessionMagnetometer);
    }
}
