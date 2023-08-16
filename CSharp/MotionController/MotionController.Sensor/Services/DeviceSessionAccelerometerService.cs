using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Services;

public interface IDeviceSessionAccelerometerService : IService
{
    Task<bool> AddDeviceSessionAccelerometerAsync(DeviceSessionAccelerometer deviceSessionAccelerometer);
}

internal class DeviceSessionAccelerometerService : ServiceBase<DeviceSessionAccelerometerService>, IDeviceSessionAccelerometerService
{
    public DeviceSessionAccelerometerService(ILogger<DeviceSessionAccelerometerService> logger, IDeviceSessionAccelerometerRepository deviceSessionAccelerometerRepository)
        : base(logger)
    {
        DeviceSessionAccelerometerRepository = deviceSessionAccelerometerRepository;
    }

    private IDeviceSessionAccelerometerRepository DeviceSessionAccelerometerRepository { get; }

    public async Task<bool> AddDeviceSessionAccelerometerAsync(DeviceSessionAccelerometer deviceSessionAccelerometer)
    {
        return await DeviceSessionAccelerometerRepository.AddAsync(deviceSessionAccelerometer);
    }
}
