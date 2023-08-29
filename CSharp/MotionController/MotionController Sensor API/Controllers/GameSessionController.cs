using Microsoft.AspNetCore.Mvc;
using MotionController.Sensor.Db.Data.Models;
using MotionController.Sensor.Models.Game;
using MotionController.Sensor.Services;
using MotionController.Services;
using NSwag.Annotations;

namespace MotionController.API.Controllers
{
    [Route("api/v1/game/sessions")]
    [OpenApiController("GameSession")]
    public class GameSessionController : ControllerBase
    {
        public GameSessionController(ILogger<GameSessionController> logger, IGameSessionService gameSessionService)
        {
            Logger = logger;
            GameSessionService = gameSessionService;
        }

        private ILogger<GameSessionController> Logger { get; }
        private IGameSessionService GameSessionService { get; }

        [HttpGet]
        [Route("{sessionId:guid}", Name = nameof(GetGameSessionBySessionIdAsync))]
        [OpenApiOperation(nameof(GetGameSessionBySessionIdAsync), "Get a Game Session by Session Id", "")]
        [ProducesResponseType(typeof(DeviceSession), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        public async Task<IActionResult> GetGameSessionBySessionIdAsync([FromRoute] Guid sessionId)
        {
            try
            {
                var deviceSession = await GameSessionService.GetGameSessionAsync(sessionId);
                if (deviceSession?.Equals(default) ?? true)
                {
                    return NotFound();
                }

                return Ok(deviceSession);
            }
            catch (Exception ex)
            {
                Logger.LogError(ex, $"{nameof(GetGameSessionBySessionIdAsync)} operation failed.");
                throw;
            }
        }

        [HttpPost]
        [Route("", Name = nameof(AddGameSessionAsync))]
        [OpenApiOperation(nameof(AddGameSessionAsync), "Adds a Game Session", "")]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<IActionResult> AddGameSessionAsync([FromBody] UnityGameSession unityGameSession)
        {
            try
            {
                var created = await GameSessionService.AddGameSessionAsync(unityGameSession);
                if (created)
                {
                    var gameSession = await GameSessionService.GetGameSessionAsync(unityGameSession.Guid);
                    
                    return CreatedAtRoute(nameof(GetGameSessionBySessionIdAsync), new { sessionId = unityGameSession.Guid }, gameSession);
                }

                return BadRequest();
            }
            catch (Exception ex)
            {
                Logger.LogError(ex, $"{nameof(AddGameSessionAsync)} operation failed.");
                throw;
            }
        }
    }
}
