using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Providers;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionPressureRepository : IRepository<DeviceSessionPressure, int>
{
}

internal class DeviceSessionPressureRepository : DbRepositoryBase<DeviceSessionPressure, int>, IDeviceSessionPressureRepository
{
    public DeviceSessionPressureRepository(IMotionProvider provider)
        : base(provider)
    {
    }

    public override Task<bool> AddAsync(DeviceSessionPressure model)
    {
        model.Created = DateTime.Now;
        model.Modified = DateTime.Now;

        return base.AddAsync(model);
    }
}
