using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using MotionController.Data;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;

namespace MotionController.Sensor.Services;

public interface IGameSessionBallPositionService : IService
{
    Task<bool> CreateGameSessionBallPositionAsync(GameSession gameSession, Vector3 ballPosition);
}

internal class GameSessionBallPositionService : ServiceBase<GameSessionBallPositionService>, IGameSessionBallPositionService
{
    public GameSessionBallPositionService(ILogger<GameSessionBallPositionService> logger, IServiceProvider serviceProvider) 
        : base(logger)
    {
        ServiceProvider = serviceProvider;
    }

    private IServiceProvider ServiceProvider { get; }

    public async Task<bool> CreateGameSessionBallPositionAsync(GameSession gameSession, Vector3 ballPosition)
    {
        if (ballPosition == default)
        {
            return false;
        }

        using var scope = ServiceProvider.CreateScope();

        var unitOfWork = scope.ServiceProvider.GetRequiredService<IUnitOfWork>();

        var gameSessionBallPositionRepository = scope.ServiceProvider.GetRequiredService<IGameSessionBallPositionRepository>();

        var gameSessionBallPosition = new GameSessionBallPosition
        {
            GameSessionId = gameSession.Id,
            X = ballPosition.X,
            Y = ballPosition.Y,
            Z = ballPosition.Z
        };

        var created = await gameSessionBallPositionRepository.AddAsync(gameSessionBallPosition);

        unitOfWork.Complete();

        return created;
    }
}
