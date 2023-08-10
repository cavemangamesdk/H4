using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Models;
using MotionController.Db.Data.Repositories;

namespace MotionController.Services;

public interface IDeviceSessionEnvironmentService : IService
{
    Task<bool> AddDeviceSessionEnvironmentAsync(DeviceSessionEnvironment deviceSessionEnvironment);
}

internal class DeviceSessionEnvironmentService : ServiceBase<DeviceSessionEnvironmentService>, IDeviceSessionEnvironmentService
{
    public DeviceSessionEnvironmentService(ILogger<DeviceSessionEnvironmentService> logger, IDeviceSessionEnvironmentRepository deviceSessionEnvironmentRepository) 
        : base(logger)
    {
        DeviceSessionEnvironmentRepository = deviceSessionEnvironmentRepository;
    }

    private IDeviceSessionEnvironmentRepository DeviceSessionEnvironmentRepository { get; }

    public async Task<bool> AddDeviceSessionEnvironmentAsync(DeviceSessionEnvironment deviceSessionEnvironment)
    {
        return await DeviceSessionEnvironmentRepository.AddAsync(deviceSessionEnvironment);
    }
}
