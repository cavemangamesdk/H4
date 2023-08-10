using Autofac;
using Autofac.Extensions.DependencyInjection;
using MotionController.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Host.UseServiceProviderFactory(new AutofacServiceProviderFactory());
builder.Host.ConfigureContainer<ContainerBuilder>(containerBuilder =>
{
    containerBuilder.RegisterMotionController()
        .WithMQTTClientBackgroundService();
});
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();

class Device
{
    public int Id { get; set; }
    public Guid SessionId { get; set; }
    public DateTime Timestamp { get; set; }
}

class DeviceOritentation
{
    public int Id { get; set; }
    public Guid DeviceSessionId { get; set; }
    public float X { get; set; }
    public float Y { get; set; }
    public float Z { get; set; }
    public DateTime Timestamp { get; set; }
}

class DeviceEnvironment
{
    public int Id { get; set; }
    public Guid DeviceSessionId { get; set; }
    public float Temp { get; set; }
    public float Humidity { get; set; }
    public float Pressure { get; set; }
    public DateTime Timestamp { get; set; }
}
