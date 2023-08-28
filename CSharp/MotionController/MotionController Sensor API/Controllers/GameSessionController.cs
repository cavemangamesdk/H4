using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using NSwag.Annotations;
using System.Globalization;
using System.Numerics;
using System.Runtime.InteropServices;

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

    public class GameSession
    {
        [JsonProperty("Guid")]
        public Guid Guid { get; set; }

        [JsonProperty("PlayerData")]
        public PlayerData? PlayerData { get; set; }

        [JsonProperty("GameData")]
        public GameData[] GameData { get; set; } = Array.Empty<GameData>();
    }

    public class PlayerData
    {
        [JsonProperty("Name")]
        public string? Name { get; set; }

        [JsonProperty("Lives")]
        public int Lives { get; set; }

        [JsonProperty("GameTime")]
        public string? GameTime { get; set; }
    }

    public class GameData
    {
        [JsonProperty("BallPosition")]
        public Vector3? BallPosition { get; set; }

        [JsonProperty("BoardRotation")]
        public Vector3? BoardRotation { get; set; }

        [JsonProperty("InputData")]
        public Vector2? InputData { get; set; }
    }

    public class Vector3
    {
        [JsonProperty("x")]
        public float X { get; set; }

        [JsonProperty("y")]
        public float Y { get; set; }

        [JsonProperty("z")]
        public float Z { get; set; }
    }

    public class Vector2
    {
        [JsonProperty("x")]
        public float X { get; set; }

        [JsonProperty("y")]
        public float Y { get; set; }
    }
}
