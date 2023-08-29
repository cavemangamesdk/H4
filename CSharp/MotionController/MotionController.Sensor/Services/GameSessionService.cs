using Microsoft.Extensions.Logging;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionService : IService
{
    Task<bool> AddGameSessionAsync(UnityGameSession gameSession);
}

internal class GameSessionService : ServiceBase<GameSessionService>, IGameSessionService
{
    public GameSessionService(ILogger<GameSessionService> logger) 
        : base(logger)
    {
    }

    public Task<bool> AddGameSessionAsync(GameSession gameSession)
    public Task<bool> AddGameSessionAsync(UnityGameSession gameSession)
    {
        throw new NotImplementedException();
    }
}
