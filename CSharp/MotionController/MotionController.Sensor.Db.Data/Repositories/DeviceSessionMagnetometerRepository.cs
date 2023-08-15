using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Providers;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionMagnetometerRepository : IRepository<DeviceSessionMagnetometer, int>
{
}

internal class DeviceSessionMagnetometerRepository : DbRepositoryBase<DeviceSessionMagnetometer, int>, IDeviceSessionMagnetometerRepository
{
    public DeviceSessionMagnetometerRepository(IMotionProvider provider)
        : base(provider)
    {
    }

    public override Task<bool> AddAsync(DeviceSessionMagnetometer model)
    {
        model.Created = DateTime.Now;
        model.Modified = DateTime.Now;

        return base.AddAsync(model);
    }
}

