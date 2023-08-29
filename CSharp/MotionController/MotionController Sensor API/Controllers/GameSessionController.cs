using Microsoft.AspNetCore.Mvc;
using MotionController.Sensor.Models.Game;
using MotionController.Sensor.Services;
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

        [HttpPost]
        [Route("", Name = nameof(AddGameSessionAsync))]
        [OpenApiOperation(nameof(AddGameSessionAsync), "Adds a Game Session", "")]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<IActionResult> AddGameSessionAsync([FromBody] UnityGameSession gameSession)
        {
            try
            {
                var created = await GameSessionService.AddGameSessionAsync(gameSession);
                if (created)
                {
                    Logger.LogInformation("Game session created successfully");
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
