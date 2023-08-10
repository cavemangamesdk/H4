using MotionController.Data.Providers.Http;
using Newtonsoft.Json;

namespace MotionController.Data.Repositories.Http;

public abstract class HttpClientRepositoryBase : RepositoryBase<IHttpClientProvider>
{
    protected HttpClientRepositoryBase(IHttpClientProvider provider)
        : base(provider)
    {
    }

    protected async Task<T?> GetJsonAsync<T>(string? requestUri, CancellationToken cancellationToken)
    {
        using var httpResponseMessage = await Provider.GetAsync(requestUri, cancellationToken);

        httpResponseMessage.EnsureSuccessStatusCode();

        var responseContent = await httpResponseMessage.Content.ReadAsStringAsync(cancellationToken);

        return DeserializeObject<T>(requestUri, responseContent);
    }

    protected virtual T? DeserializeObject<T>(string? requestUri, string responseContent)
    {
        return JsonConvert.DeserializeObject<T>(responseContent);
    }
}
