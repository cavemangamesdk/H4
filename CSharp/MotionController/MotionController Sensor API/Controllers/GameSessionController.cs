using Microsoft.AspNetCore.Mvc;
using NSwag.Annotations;
using System.Globalization;

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
        public async Task<IActionResult> AddGameSessionAsync()
        {
            try
            {
                var timeStr = "01:28:31";

                var time = TimeSpan.Parse(timeStr);

                var timeExact = TimeSpan.ParseExact(timeStr, @"m\:s\:ff", CultureInfo.InvariantCulture);

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
