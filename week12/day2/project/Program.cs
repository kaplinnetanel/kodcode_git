using System;
namespace project;
 
abstract class Platform
{
    private  int _trackId;
    private double _speedKnots;
    private double _heading;


    public int TrackId
    {
        get { return _trackId; }
        protected set
        {
            if (value > 0)
            {
                _trackId = value;
            }
        }
    }

    public double SpeedKnots
    {
        get { return _speedKnots; }
        set
        { if (value >= 0 && value <= 359)
            {
                _speedKnots = value;
            }    
        }
    }
    public double Heading
    {
        get { return _heading; }
        set
        {
            if (value > 0)
            { _heading = value; }
        }
    }
    public Platform(int trackId,double speedKnots,double heading)
    {
        TrackId = trackId;
        SpeedKnots = speedKnots;
        Heading = heading;
    }
    abstract public string StatusLine();
    abstract public bool IsTrackable();

}


class AirPlatform : Platform
{
    public double AltitudeFeet { get; set; }

    public AirPlatform(int trackId, double speedKnots, double heading, double altitudeFeet) : base(trackId,speedKnots,heading)
    {
        AltitudeFeet = altitudeFeet;

    }
    public override bool IsTrackable()
    {
        if (SpeedKnots > 0 && SpeedKnots < 60000)
        {
            return true;
        }
        return false;
    }
    public override string StatusLine()
    {
        return $"ID: {TrackId}, Speed: {SpeedKnots}kts, Heading: {Heading}°";
    }

}

class SeaPlatform : Platform
{
    private double DepthMeters { get; set; }

    public SeaPlatform(int trackId, double speedKnots, double heading, double depthMeters) : base(trackId,speedKnots,heading)
    {
        DepthMeters = depthMeters;
    }

    public override bool IsTrackable()
    {
        if (DepthMeters >= 0 && DepthMeters <= 359)
        {
            return true;
        }
        return false;

    }
    public override string StatusLine()
    {
        return $"ID: {TrackId}, Speed: {SpeedKnots}kts, Heading: {Heading}°";
    }
}

class GroundPlatform : Platform
{
    private string TerrainType { get; set; }

    public GroundPlatform(int trackId, double speedKnots, double heading, string terrainType) : base(trackId,speedKnots,heading)
    {
        TerrainType = terrainType;
    }

    public override bool IsTrackable()
    {
        if (TerrainType != "tunnel" )
        {
            return true;
        }
        return false;

    }
    public override string StatusLine()
    {
        return $"ID: {TrackId}, Speed: {SpeedKnots}kts, Heading: {Heading}°";
    }
}
class Program
{
    static void Main()
    {
        Platform air = new AirPlatform(1, 50, 90, 5000);
        Platform air1 = new AirPlatform(2, 0, 0, 50);
        Platform sea = new SeaPlatform(3, 10, 180, 50);
        Platform groun = new GroundPlatform(5, 20, 45, "netanel");
        Platform groun1 = new GroundPlatform(6, 0, 0, "tunnel");
        List<Platform> platforms = new List<Platform>
            {
             air,air1,sea, groun,groun1
            };

        foreach (Platform p in platforms)
        {
            Console.WriteLine($"{p.StatusLine()} | Reliable: {p.IsTrackable()}");
        }
    }
}



