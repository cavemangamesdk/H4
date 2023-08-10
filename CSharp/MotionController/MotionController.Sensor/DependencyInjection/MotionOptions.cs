using MotionController.Data.Providers.Database.SqlClient;

namespace MotionController.Extensions.DependencyInjection;

public class MotionOptions
{
    public const string Motion = "MotionController";

    public SqlClientProviderSettings? SqlClientProviderSettings { get; set; }
}
