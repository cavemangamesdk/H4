using Microsoft.Extensions.Logging;
using System.Collections.Concurrent;
using System.Data;
using System.Web;
using VictorKrogh.Extensions.System;

namespace MotionController.Data.Providers.Http;

public interface IHttpClientProvider : IProvider
{
    Task<HttpResponseMessage> GetAsync(string? requestUri, CancellationToken cancellationToken);
}

public class HttpClientProviderBase : ProviderBase, IHttpClientProvider
{
    private static readonly ConcurrentDictionary<string, Uri?> RequestUriCache = new();
    private HttpClient? httpClient;

    public HttpClientProviderBase(ILogger<HttpClientProviderBase> logger, IHttpClientFactory httpClientFactory, HttpClientProviderSettings httpClientProviderSettings)
        : base(IsolationLevel.Unspecified)
    {
        Logger = logger;
        HttpClientFactory = httpClientFactory;
        HttpClientProviderSettings = httpClientProviderSettings;
    }

    private ILogger<HttpClientProviderBase> Logger { get; }
    private IHttpClientFactory HttpClientFactory { get; }
    protected HttpClientProviderSettings HttpClientProviderSettings { get; }

    private HttpClient HttpClient => httpClient ??= CreateHttpClient();

    private HttpClient CreateHttpClient()
    {
        var httpClient = HttpClientFactory.CreateClient(GetType().Name);

        httpClient.BaseAddress = CreateBaseAddress();
        httpClient.Timeout = HttpClientProviderSettings.Timeout;
        httpClient.MaxResponseContentBufferSize = HttpClientProviderSettings.MaxResponseContentBufferSize;

        foreach (var requestHeader in HttpClientProviderSettings.DefaultRequestHeaders)
        {
            httpClient.DefaultRequestHeaders.Add(requestHeader.Key, requestHeader.Value);
        }

        return httpClient;
    }

    private Uri? CreateBaseAddress()
    {
        var baseAddress = default(Uri);

        if (HttpClientProviderSettings.BaseAddress == null)
        {
            baseAddress = new Uri(string.Empty);
        }
        else
        {
            var httpValueCollection = HttpUtility.ParseQueryString(HttpClientProviderSettings.BaseAddress.Query);

            foreach (var queryString in HttpClientProviderSettings.DefaultQueryStrings)
            {
                httpValueCollection.Remove(queryString.Key);
                httpValueCollection.Add(queryString.Key, queryString.Value);
            }

            var uriBuilder = new UriBuilder(HttpClientProviderSettings.BaseAddress)
            {
                Query = httpValueCollection.ToString()
            };

            baseAddress = uriBuilder.Uri;
        }

        return baseAddress;
    }

    protected Uri? BuildRequestUri(string? requestUri)
    {
        return RequestUriCache.GetOrAdd(requestUri ?? string.Empty, uri =>
        {
            if (string.IsNullOrWhiteSpace(uri))
            {
                return HttpClient.BaseAddress;
            }

            var baseUri = new Uri(new Uri(HttpClient.BaseAddress?.GetComponents(UriComponents.SchemeAndServer | UriComponents.Path, UriFormat.SafeUnescaped) ?? string.Empty), uri);

            var uriBuilder = new UriBuilder(baseUri);

            uriBuilder.AddQueryStrings(HttpClient.BaseAddress?.Query ?? string.Empty);

            return uriBuilder.Uri;
        });
    }

    public async Task<HttpResponseMessage> GetAsync(string? requestUri, CancellationToken cancellationToken)
    {
        var uri = BuildRequestUri(requestUri);

        var httpResponseMessage = await HttpClient.GetAsync(uri, cancellationToken);

        await LogUnsuccessfulResponseAsync(uri, httpResponseMessage, cancellationToken);

        return httpResponseMessage;
    }

    private async Task LogUnsuccessfulResponseAsync(Uri? uri, HttpResponseMessage httpResponseMessage, CancellationToken cancellationToken)
    {
        if (httpResponseMessage.IsSuccessStatusCode)
        {
            return;
        }

        switch (httpResponseMessage.StatusCode)
        {
            case System.Net.HttpStatusCode.Ambiguous:
            case System.Net.HttpStatusCode.Moved:
            case System.Net.HttpStatusCode.Found:
            case System.Net.HttpStatusCode.RedirectMethod:
            case System.Net.HttpStatusCode.NotModified:
            case System.Net.HttpStatusCode.UseProxy:
            case System.Net.HttpStatusCode.Unused:
            case System.Net.HttpStatusCode.RedirectKeepVerb:
            case System.Net.HttpStatusCode.PermanentRedirect:
                Logger.LogInformation($"Post request responsed with status code {httpResponseMessage.StatusCode}. URI: {uri?.AbsoluteUri}; Reason: {httpResponseMessage.ReasonPhrase}; Content: {await httpResponseMessage.Content.ReadAsStringAsync(cancellationToken)}");
                break;
            case System.Net.HttpStatusCode.BadRequest:
            case System.Net.HttpStatusCode.Unauthorized:
            case System.Net.HttpStatusCode.PaymentRequired:
            case System.Net.HttpStatusCode.Forbidden:
            case System.Net.HttpStatusCode.NotFound:
            case System.Net.HttpStatusCode.MethodNotAllowed:
            case System.Net.HttpStatusCode.NotAcceptable:
            case System.Net.HttpStatusCode.ProxyAuthenticationRequired:
            case System.Net.HttpStatusCode.RequestTimeout:
            case System.Net.HttpStatusCode.Conflict:
            case System.Net.HttpStatusCode.Gone:
            case System.Net.HttpStatusCode.LengthRequired:
            case System.Net.HttpStatusCode.PreconditionFailed:
            case System.Net.HttpStatusCode.RequestEntityTooLarge:
            case System.Net.HttpStatusCode.RequestUriTooLong:
            case System.Net.HttpStatusCode.UnsupportedMediaType:
            case System.Net.HttpStatusCode.RequestedRangeNotSatisfiable:
            case System.Net.HttpStatusCode.ExpectationFailed:
            case System.Net.HttpStatusCode.MisdirectedRequest:
            case System.Net.HttpStatusCode.UnprocessableEntity:
            case System.Net.HttpStatusCode.Locked:
            case System.Net.HttpStatusCode.FailedDependency:
            case System.Net.HttpStatusCode.UpgradeRequired:
            case System.Net.HttpStatusCode.PreconditionRequired:
            case System.Net.HttpStatusCode.TooManyRequests:
            case System.Net.HttpStatusCode.RequestHeaderFieldsTooLarge:
            case System.Net.HttpStatusCode.UnavailableForLegalReasons:
                Logger.LogWarning($"Post request failed with status code {httpResponseMessage.StatusCode}. URI: {uri?.AbsoluteUri}; Reason: {httpResponseMessage.ReasonPhrase}; Content: {await httpResponseMessage.Content.ReadAsStringAsync(cancellationToken)}");
                break;
            case System.Net.HttpStatusCode.InternalServerError:
            case System.Net.HttpStatusCode.NotImplemented:
            case System.Net.HttpStatusCode.BadGateway:
            case System.Net.HttpStatusCode.ServiceUnavailable:
            case System.Net.HttpStatusCode.GatewayTimeout:
            case System.Net.HttpStatusCode.HttpVersionNotSupported:
            case System.Net.HttpStatusCode.VariantAlsoNegotiates:
            case System.Net.HttpStatusCode.InsufficientStorage:
            case System.Net.HttpStatusCode.LoopDetected:
            case System.Net.HttpStatusCode.NotExtended:
            case System.Net.HttpStatusCode.NetworkAuthenticationRequired:
                Logger.LogError($"Post request failed with status code {httpResponseMessage.StatusCode}. URI: {uri?.AbsoluteUri}; Reason: {httpResponseMessage.ReasonPhrase}; Content: {await httpResponseMessage.Content.ReadAsStringAsync(cancellationToken)}");
                break;
            default:
                break;
        }
    }

    protected override void DisposeManagedState()
    {
        if (httpClient != null)
        {
            httpClient.Dispose();
        }
    }
}
