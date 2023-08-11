using Microsoft.Extensions.DependencyInjection;

namespace MotionController.MQTT.Messages
{
    public interface IMessageHandler
    {
        Task HandleAsync(object model);
    }

    public interface IMessageHandler<TModel> : IMessageHandler
    {
    }

    public abstract class MessageHandlerBase<TModel> : IMessageHandler<TModel>
    {
        public MessageHandlerBase(IServiceProvider serviceProvider)
        {
            ServiceProvider = serviceProvider;
        }

        protected IServiceProvider ServiceProvider { get; }

        public Task HandleAsync(object model)
        {
            if (model is TModel castedModel)
            {
                using var scope = ServiceProvider.CreateScope();

                return HandleModelAsync(castedModel);
            }

            throw new InvalidCastException("Model is invald!");
        }

        protected abstract Task HandleModelAsync(TModel model);
    }
}
