using Autofac;
using Autofac.Extensions.DependencyInjection;
using MotionController.Extensions.DependencyInjection;
using VictorKrogh.Extensions.Autofac;

var builder = WebApplication.CreateBuilder(args);

builder.Configuration.SetBasePath(builder.Environment.ContentRootPath)
    .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
    .AddJsonFile($"appsettings.{builder.Environment.EnvironmentName}.json", optional: true);

var weatherOptions = builder.Configuration.GetSection(MotionOptions.Motion).Get<MotionOptions>();

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Host.UseServiceProviderFactory(new AutofacServiceProviderFactory());
builder.Host.ConfigureContainer<ContainerBuilder>(containerBuilder =>
{
    containerBuilder.RegisterMotionController(weatherOptions)
        .WithMQTTClientBackgroundService();

    containerBuilder.RegisterUnitOfWorkFactory();
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
