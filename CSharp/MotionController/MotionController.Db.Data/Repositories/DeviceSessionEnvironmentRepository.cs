using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Models;
using MotionController.Db.Data.Providers;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionEnvironmentRepository : IRepository<DeviceSessionEnvironment, int>
{
}

internal class DeviceSessionEnvironmentRepository : DbRepositoryBase<DeviceSessionEnvironment, int>, IDeviceSessionEnvironmentRepository
{
    public DeviceSessionEnvironmentRepository(IMotionProvider provider) 
        : base(provider)
    {
    }
}
