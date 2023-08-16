using Microsoft.AspNetCore.Mvc;
using MotionController.Db.Data.Models;
using MotionController.Services;
using NSwag.Annotations;

namespace MotionController.API.Controllers
{
    [Route("api/v1/device/sessions")]
    [OpenApiController("DeviceSession")]
    public class DeviceSessionController : ControllerBase
    {
        public DeviceSessionController(ILogger<DeviceSessionController> logger, IDeviceSessionService deviceSessionService)
        {
            Logger = logger;
            DeviceSessionService = deviceSessionService;
        }

        private ILogger<DeviceSessionController> Logger { get; }
        private IDeviceSessionService DeviceSessionService { get; }

        [HttpGet]
        [Route("", Name = nameof(GetDeviceSessionsAsync))]
        [OpenApiOperation(nameof(GetDeviceSessionsAsync), "Gets all Device Sessions", "")]
        [ProducesResponseType(typeof(IEnumerable<DeviceSession>), StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        public async Task<IActionResult> GetDeviceSessionsAsync()
        {
            try
            {
                var deviceSessions = await DeviceSessionService.GetDeviceSessionsAsync();
                if (deviceSessions == default)
                {
                    deviceSessions = Array.Empty<DeviceSession>();
                }

                return Ok(deviceSessions);
            }
            catch (Exception ex)
            {
                Logger.LogError(ex, $"{nameof(GetDeviceSessionsAsync)} operation failed.");
                throw;
            }
        }

    }
}
