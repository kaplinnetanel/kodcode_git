using System;

class Track
{
    public int Id;
    public double Speed;
    public double Heading;

    public Track(int id, double speed, double heading)
    {
        Id = id;
        Speed = speed;
        Heading = heading;
    }

    public Track(int id) : this(id, 0.0, 0.0)
    {
    }
    public void Print()
    {
        Console.WriteLine($"Track ID: {Id}, Speed: {Speed} kn, Heading: {Heading}°");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Track full = new Track(17, 412.5, 270);
        Track quick = new Track(8);

        // שימוש במתודת ההדפסה
        full.Print();
        quick.Print();
    }
}