namespace MotionController.MQTT;

[AttributeUsage(AttributeTargets.Class, AllowMultiple = false)]
public sealed class MQTTTopicAttribute : Attribute
{
    public MQTTTopicAttribute(string topic)
    {
        Topic = topic;
    }

    public string Topic { get; }
}
