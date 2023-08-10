using MotionController.Data.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace MotionController.Db.Data.Models;

[Schema("H4")]
[Table("DeviceSessionEnvironment")]
public class DeviceSessionEnvironment : DatabaseModel
{
    [Key]
    [Column("Id")]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int Id { get; set; }

    [Column("SessionId")]
    public Guid SessionId { get; set; }

    [Column("TemperatureCelsius")]
    public float TemperatureCelsius { get; set; }

    [Column("HumidityPercentage")]
    public float HumidityPercentage { get; set; }

    [Column("PressureMillibars")]
    public float PressureMillibars { get; set; }

    [Column("Timestamp")]
    public DateTime Timestamp { get; set; }

    [Column("Created")]
    public DateTime Created { get; set; }

    [Column("Modified")]
    public DateTime Modified { get; set; }
}
