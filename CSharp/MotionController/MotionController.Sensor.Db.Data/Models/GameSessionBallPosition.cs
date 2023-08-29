using MotionController.Data.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace MotionController.Sensor.Db.Data.Models;

[Schema("H4")]
[Table("GameSessionBallPosition")]
public sealed class GameSessionBallPosition : DatabaseModel
{
    [Key]
    [Column("Id")]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int Id { get; set; }

    [Column("GameSession_Id")]
    public int GameSessionId { get; set; }

    [Column("X")]
    public decimal X { get; set; }

    [Column("Y")]
    public decimal Y { get; set; }

    [Column("Z")]
    public decimal Z { get; set; }

    [Column("Created")]
    public DateTime Created { get; set; }

    [Column("Modified")]
    public DateTime Modified { get; set; }
}
