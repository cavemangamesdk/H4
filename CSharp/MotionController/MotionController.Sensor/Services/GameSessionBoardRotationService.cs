using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionBoardRotationService : IService
{
    Task<bool> CreateGameSessionBoardRotationAsync(GameSession gameSession, Vector3 boardRotation);
}

internal class GameSessionBoardRotationService : ServiceBase<GameSessionBoardRotationService>, IGameSessionBoardRotationService
{
    public GameSessionBoardRotationService(ILogger<GameSessionBoardRotationService> logger, IServiceProvider serviceProvider) 
        : base(logger)
    {
        ServiceProvider = serviceProvider;
    }

    private IServiceProvider ServiceProvider { get; }

    public async Task<bool> CreateGameSessionBoardRotationAsync(GameSession gameSession, Vector3 boardRotation)
    {
        if (boardRotation == default)
        {
            return false;
        }

        using var scope = ServiceProvider.CreateScope();

        var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

        var gameSessionBoardRotationRepository = scope.ServiceProvider.GetRequiredService<IGameSessionBoardRotationRepository>();

        var gameSessionBoardRotation = new GameSessionBoardRotation
        {
            GameSessionId = gameSession.Id,
            X = boardRotation.X,
            Y = boardRotation.Y,
            Z = boardRotation.Z
        };

        var created = await gameSessionBoardRotationRepository.AddAsync(gameSessionBoardRotation);

        unitOfWork.Complete();

        return created;
    }
}
