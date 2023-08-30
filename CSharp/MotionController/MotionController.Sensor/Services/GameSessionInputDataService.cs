using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionInputDataService : IService
{
    Task<bool> AddGameSessionInputDataAsync(GameSession gameSession, Vector2 inputData);
}

internal class GameSessionInputDataService : ServiceBase<GameSessionInputDataService>, IGameSessionInputDataService
{
    public GameSessionInputDataService(ILogger<GameSessionInputDataService> logger, IGameSessionInputDataRepository gameSessionInputDataRepository) 
        : base(logger)
    {
        GameSessionInputDataRepository = gameSessionInputDataRepository;
    }

    private IGameSessionInputDataRepository GameSessionInputDataRepository { get; }

    public async Task<bool> AddGameSessionInputDataAsync(GameSession gameSession, Vector2 inputData)
    {
        if (inputData == default)
        {
            return false;
        }

        var gameSessionInputData = new GameSessionInputData
        {
            GameSessionId = gameSession.Id,
            X = inputData.X,
            Y = inputData.Y,
        };

        return await GameSessionInputDataRepository.AddAsync(gameSessionInputData);
    }
}
