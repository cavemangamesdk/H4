using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using System.Data;
using System.Reflection;

namespace MotionController.Data.Providers.Http;

public class HttpClientProviderFactory<TProvider> : IProviderFactory<TProvider>
    where TProvider : IHttpClientProvider
{
    public HttpClientProviderFactory(IServiceProvider serviceProvider, IHttpClientFactory httpClientFactory, HttpClientProviderSettings httpClientProviderSettings)
    {
        ServiceProvider = serviceProvider;
        HttpClientFactory = httpClientFactory;
        HttpClientProviderSettings = httpClientProviderSettings;
    }

    protected IServiceProvider ServiceProvider { get; }
    protected IHttpClientFactory HttpClientFactory { get; }
    protected HttpClientProviderSettings HttpClientProviderSettings { get; }

    public TProvider CreateProvider(IsolationLevel isolationLevel = IsolationLevel.ReadCommitted)
    {
        var type = typeof(TProvider);

        var ctor = type.GetConstructor(BindingFlags.Instance | BindingFlags.Public, null, new[] { typeof(ILogger<TProvider>), typeof(IHttpClientFactory), typeof(HttpClientProviderSettings) }, null);
        if (ctor == null)
        {
            throw new NotImplementedException("Constructor not implemented.");
        }

        var logger = ServiceProvider.GetRequiredService<ILogger<TProvider>>();

        var instance = ctor.Invoke(new object[] { logger, HttpClientFactory, HttpClientProviderSettings });

        return (TProvider)instance;
    }
}
