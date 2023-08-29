using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionBoardRotationService : IService
{
    Task<bool> AddGameSessionBoardRotationAsync(GameSession gameSession, Vector3 boardRotation);
}

internal class GameSessionBoardRotationService : ServiceBase<GameSessionBoardRotationService>, IGameSessionBoardRotationService
{
    public GameSessionBoardRotationService(ILogger<GameSessionBoardRotationService> logger, IGameSessionBoardRotationRepository gameSessionBoardRotationRepository) 
        : base(logger)
    {
        GameSessionBoardRotationRepository = gameSessionBoardRotationRepository;
    }

    private IGameSessionBoardRotationRepository GameSessionBoardRotationRepository { get; }

    public async Task<bool> AddGameSessionBoardRotationAsync(GameSession gameSession, Vector3 boardRotation)
    {
        if (boardRotation == default)
        {
            return false;
        }

        var gameSessionBoardRotation = new GameSessionBoardRotation
        {
            GameSessionId = gameSession.Id,
            X = boardRotation.X,
            Y = boardRotation.Y,
            Z = boardRotation.Z
        };

        return await GameSessionBoardRotationRepository.AddAsync(gameSessionBoardRotation);
    }
}
