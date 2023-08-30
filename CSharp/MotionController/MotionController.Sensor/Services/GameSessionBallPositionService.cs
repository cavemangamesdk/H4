using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionBallPositionService : IService
{
    Task<bool> AddGameSessionBallPositionAsync(GameSession gameSession, Vector3 ballPosition);
}

internal class GameSessionBallPositionService : ServiceBase<GameSessionBallPositionService>, IGameSessionBallPositionService
{
    public GameSessionBallPositionService(ILogger<GameSessionBallPositionService> logger, IGameSessionBallPositionRepository gameSessionBallPositionRepository) 
        : base(logger)
    {
        GameSessionBallPositionRepository = gameSessionBallPositionRepository;
    }

    private IGameSessionBallPositionRepository GameSessionBallPositionRepository { get; }

    public async Task<bool> AddGameSessionBallPositionAsync(GameSession gameSession, Vector3 ballPosition)
    {
        if (ballPosition == default)
        {
            return false;
        }

        var gameSessionBallPosition = new GameSessionBallPosition
        {
            GameSessionId = gameSession.Id,
            X = ballPosition.X,
            Y = ballPosition.Y,
            Z = ballPosition.Z
        };

        return await GameSessionBallPositionRepository.AddAsync(gameSessionBallPosition);
    }
}
