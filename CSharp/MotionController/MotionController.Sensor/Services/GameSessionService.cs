using Microsoft.Extensions.Logging;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Db.Data.Repositories;
using MotionController.Sensor.Models.Game;
using MotionController.Services;
using System.Globalization;

namespace MotionController.Sensor.Services;

public interface IGameSessionService : IService
{
    Task<GameSession?> GetGameSessionAsync(Guid sessionId);
    Task<bool> AddGameSessionAsync(UnityGameSession gameSession);
}

internal class GameSessionService : ServiceBase<GameSessionService>, IGameSessionService
{
    private const string GameTimeFormat = @"m\:s\:ff";

    public GameSessionService(ILogger<GameSessionService> logger, IGameSessionRepository gameSessionRepository) 
        : base(logger)
    {
        GameSessionRepository = gameSessionRepository;
    }

    private IGameSessionRepository GameSessionRepository { get; }

    public async Task<GameSession?> GetGameSessionAsync(Guid sessionId)
    {
        return await GameSessionRepository.GetAsync(sessionId);
    }

    public async Task<bool> AddGameSessionAsync(UnityGameSession unityGameSession)
    {
        if(!TimeSpan.TryParseExact(unityGameSession?.PlayerData?.GameTime ?? string.Empty, GameTimeFormat, CultureInfo.InvariantCulture, out var gameTimeSpan))
        {
            return false;
        }

        if(unityGameSession == default)
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

        return await GameSessionRepository.AddAsync(gameSession);
    }
}
