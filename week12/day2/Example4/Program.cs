using System;
using System.Collections.Generic;

// --- הבסיס ---
abstract class Track
{
    public int Id { get; }
    public double Speed { get; set; }
    protected Track(int id, double speed) { Id = id; Speed = speed; }
    public abstract string Describe();
}

// --- סוגים קונקרטיים ---
class Aircraft : Track
{
    public double Altitude { get; }
    public Aircraft(int id, double speed, double altitude) : base(id, speed) => Altitude = altitude;
    public override string Describe() => $"Aircraft {Id} at {Altitude} ft, {Speed} kn";
}

class Vessel : Track
{
    public Vessel(int id, double speed) : base(id, speed) { }
    public override string Describe() => $"Vessel {Id}, {Speed} kn";
}

// הוספנו סוג שלישי כדי לראות את הקסם בפעולה
class Drone : Track
{
    public Drone(int id, double speed) : base(id, speed) { }
    public override string Describe() => $"Drone {Id} (Stealth Mode), {Speed} kn";
}

class Program
{
    static void Main()
    {
        // יצירת רשימה פולימורפית
        List<Track> all = new()
        {
            new Aircraft(1, 420, 30000),
            new Vessel(2, 18),
            new Aircraft(3, 510, 41000),
            new Drone(4, 50) // הוספנו את הסוג החדש בקלות
        };

        // הלולאה לא השתנתה, היא פשוט "קראה" למתודה של כל אובייקט
        foreach (Track t in all)
        {
            Console.WriteLine(t.Describe());
        }
    }
}