using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Providers;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionAccelerometerRepository : IRepository<DeviceSessionAccelerometer, int>
{
}

internal class DeviceSessionAccelerometerRepository : DbRepositoryBase<DeviceSessionAccelerometer, int>, IDeviceSessionAccelerometerRepository
{
    public DeviceSessionAccelerometerRepository(IMotionProvider provider)
        : base(provider)
    {
    }

    public override Task<bool> AddAsync(DeviceSessionAccelerometer model)
    {
        model.Created = DateTime.Now;
        model.Modified = DateTime.Now;

        return base.AddAsync(model);
    }
}

