﻿using Microsoft.AspNetCore.Mvc;
using MotionController.Sensor.Models.Game;
using NSwag.Annotations;

namespace MotionController.API.Controllers
{
    [Route("api/v1/game/sessions")]
    [OpenApiController("GameSession")]
    public class GameSessionController : ControllerBase
    {
        public GameSessionController(ILogger<GameSessionController> logger)
        {
            Logger = logger;
        }

        private ILogger<GameSessionController> Logger { get; }

        [HttpPost]
        [Route("", Name = nameof(AddGameSessionAsync))]
        [OpenApiOperation(nameof(AddGameSessionAsync), "Adds a Game Session", "")]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<IActionResult> AddGameSessionAsync([FromBody] GameSession gameSession)
        {
            try
            {
                Logger.LogError("sdfogfgjiog", gameSession);

                return await Task.FromResult(Ok());
            }
            catch (Exception ex)
            {
                Logger.LogError(ex, $"{nameof(AddGameSessionAsync)} operation failed.");
                throw;
            }
        }
    }
}
