using MotionController.Data.Repositories;
using MotionController.Data.Repositories.Database;
using MotionController.Db.Data.Providers;
using MotionController.Sensor.Db.Data.Models;

namespace MotionController.Db.Data.Repositories;

public interface IDeviceSessionHumidityRepository : IRepository<DeviceSessionHumidity, int>
{
    Task<IEnumerable<DeviceSessionHumidity?>> GetByDeviceSessionAsync(int deviceSessionId);
}

internal class DeviceSessionHumidityRepository : DbRepositoryBase<DeviceSessionHumidity, int>, IDeviceSessionHumidityRepository
{
    public DeviceSessionHumidityRepository(IMotionProvider provider)
        : base(provider)
    {
    }

    public async Task<IEnumerable<DeviceSessionHumidity?>> GetByDeviceSessionAsync(int deviceSessionId)
    {
        var query = $@"SELECT * FROM {Provider.GetQualifiedTableName<DeviceSessionHumidity>()} WHERE ( [DeviceSession_Id] = @deviceSessionId )";

        return await QueryAsync(query, new { @deviceSessionId });
    }

    public override Task<bool> AddAsync(DeviceSessionHumidity model)
    {
        model.Created = DateTime.Now;
        model.Modified = DateTime.Now;

        return base.AddAsync(model);
    }
}

