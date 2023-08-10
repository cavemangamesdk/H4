namespace MotionController.Data.Providers.Http;

public class HttpClientProviderSettings
{
    public HttpClientProviderSettings()
    {
        DefaultRequestHeaders = new Dictionary<string, IEnumerable<string>>();
        DefaultQueryStrings = new Dictionary<string, string>();
    }

    public Uri? BaseAddress { get; set; }
    public long MaxResponseContentBufferSize { get; set; } = int.MaxValue;
    public TimeSpan Timeout { get; set; } = TimeSpan.FromSeconds(120);
    public IDictionary<string, IEnumerable<string>> DefaultRequestHeaders { get; set; }
    public IDictionary<string, string> DefaultQueryStrings { get; set; }
}