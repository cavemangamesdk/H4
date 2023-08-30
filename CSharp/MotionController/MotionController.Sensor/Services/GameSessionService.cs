using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;
using System.Globalization;

namespace MotionController.Sensor.Services;

public interface IGameSessionService : IService
{
    Task<IEnumerable<GameSession?>> GetGameSessionsAsync();
    Task<GameSession?> GetGameSessionAsync(Guid sessionId);
    Task<bool> AddUnityGameSessionAsync(UnityGameSession gameSession);
}

internal class GameSessionService : ServiceBase<GameSessionService>, IGameSessionService
{
    private const string GameTimeFormat = @"m\:s\:ff";

    public GameSessionService(ILogger<GameSessionService> logger, IGameSessionRepository gameSessionRepository, IGameSessionBallPositionService gameSessionBallPositionService, IGameSessionBoardRotationService gameSessionBoardRotationService, IGameSessionInputDataService gameSessionInputDataService)
        : base(logger)
    {
        GameSessionRepository = gameSessionRepository;
        GameSessionBallPositionService = gameSessionBallPositionService;
        GameSessionBoardRotationService = gameSessionBoardRotationService;
        GameSessionInputDataService = gameSessionInputDataService;
    }

    private IGameSessionRepository GameSessionRepository { get; }
    private IGameSessionBallPositionService GameSessionBallPositionService { get; }
    private IGameSessionBoardRotationService GameSessionBoardRotationService { get; }
    private IGameSessionInputDataService GameSessionInputDataService { get; }

    public async Task<IEnumerable<GameSession?>> GetGameSessionsAsync()
    {
        return await GameSessionRepository.GetAsync();
    }

    public async Task<GameSession?> GetGameSessionAsync(Guid sessionId)
    {
        return await GameSessionRepository.GetAsync(sessionId);
    }

    public async Task<bool> AddUnityGameSessionAsync(UnityGameSession unityGameSession)
    {
        if (!TimeSpan.TryParseExact(unityGameSession?.PlayerData?.GameTime ?? string.Empty, GameTimeFormat, CultureInfo.InvariantCulture, out var gameTimeSpan))
        {
            return false;
        }

        if (unityGameSession == default)
        {
            return false;
        }

        var gameSession = new GameSession
        {
            SessionId = unityGameSession.Guid,
            PlayerName = unityGameSession.PlayerData?.Name ?? string.Empty,
            Lives = unityGameSession.PlayerData?.Lives ?? default,
            GameTime = gameTimeSpan
        };

        var gameSessionCreated = await GameSessionRepository.AddAsync(gameSession);
        if (!gameSessionCreated)
        {
            return false;
        }

        foreach (var gameData in unityGameSession.GameData)
        {
            if (gameData == default)
            {
                continue;
            }

            var ballPositionCreated = await GameSessionBallPositionService.AddGameSessionBallPositionAsync(gameSession, gameData.BallPosition);

            var boardRotationCreated = await GameSessionBoardRotationService.AddGameSessionBoardRotationAsync(gameSession, gameData.BoardRotation);

            var inputDataCreated = await GameSessionInputDataService.AddGameSessionInputDataAsync(gameSession, gameData.InputData);
        }

        return true;
    }
}
