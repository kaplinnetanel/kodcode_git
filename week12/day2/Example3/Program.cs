using System;

// מחלקה מופשטת - לא ניתן ליצור ממנה מופע ישירות
abstract class Track
{
    public int Id { get; }
    public double Speed { get; set; }

    // protected - רק מחלקות יורשות יכולות לקרוא לבנאי הזה
    protected Track(int id, double speed)
    {
        Id = id;
        Speed = speed;
    }

    // מתודה מופשטת - כל מחלקה יורשת חייבת להגדיר (לממש) אותה בעצמה
    public abstract string Describe();
}

class Aircraft : Track
{
    public double Altitude { get; }

    public Aircraft(int id, double speed, double altitude)
        : base(id, speed) => Altitude = altitude;

    public override string Describe()
        => $"Aircraft {Id} at {Altitude} ft, {Speed} kn";
}

class Vessel : Track
{
    public Vessel(int id, double speed) : base(id, speed) { }

    public override string Describe()
        => $"Vessel {Id}, {Speed} kn";
}

class Program
{
    static void Main()
    {
        // Aircraft a = new Aircraft(1, 420, 30000);
        // Track t = new Track(1, 100); // זה יזרוק שגיאת קומפילציה כפי שציינת

        // יצירת מופעים תקינים
        Aircraft a = new Aircraft(1, 420, 30000);
        Vessel v = new Vessel(2, 25);

        // הדפסה
        Console.WriteLine(a.Describe());
        Console.WriteLine(v.Describe());
    }
}
