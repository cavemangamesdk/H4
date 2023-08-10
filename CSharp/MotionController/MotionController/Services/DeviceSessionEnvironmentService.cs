using Microsoft.Extensions.Logging;
using MotionController.Db.Data.Repositories;

namespace MotionController.Services;

public interface IDeviceSessionEnvironmentService : IService
{
}

internal class DeviceSessionEnvironmentService : ServiceBase<DeviceSessionEnvironmentService>, IDeviceSessionEnvironmentService
{
    public DeviceSessionEnvironmentService(ILogger<DeviceSessionEnvironmentService> logger, IDeviceSessionEnvironmentRepository deviceSessionEnvironmentRepository) 
        : base(logger)
    {
        DeviceSessionEnvironmentRepository = deviceSessionEnvironmentRepository;
    }

    private IDeviceSessionEnvironmentRepository DeviceSessionEnvironmentRepository { get; }
}
