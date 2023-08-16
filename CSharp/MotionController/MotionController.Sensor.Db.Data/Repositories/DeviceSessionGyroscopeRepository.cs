﻿using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Providers;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionGyroscopeRepository : IRepository<DeviceSessionGyroscope, int>
{
}

internal class DeviceSessionGyroscopeRepository : DbRepositoryBase<DeviceSessionGyroscope, int>, IDeviceSessionGyroscopeRepository
{
    public DeviceSessionGyroscopeRepository(IMotionProvider provider)
        : base(provider)
    {
    }

    public override Task<bool> AddAsync(DeviceSessionGyroscope model)
    {
        model.Created = DateTime.Now;
        model.Modified = DateTime.Now;

        return base.AddAsync(model);
    }
}
