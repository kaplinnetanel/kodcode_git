using System;

class Track
{
    public int Id { get; }

    public Track(int id)
    {
        Id = id;
    }

    // virtual: מאפשר למחלקות יורשות לדרוס (להחליף) את המימוש הזה
    public virtual string Describe()
    {
        return $"Track {Id}";
    }
}

class Aircraft : Track
{
    public double Altitude { get; }

    public Aircraft(int id, double altitude) : base(id)
    {
        Altitude = altitude;
    }

    // override: מחליף את ההתנהגות של המחלקה הבסיסית עבור המופע הזה
    public override string Describe()
    {
        return $"Aircraft {Id} at {Altitude} ft";
    }
}

// דוגמה להרצה:
class Program
{
    static void Main()
    {
        Track t = new Track(101);
        Aircraft a = new Aircraft(1, 30000);

        // הדפסה רגילה
        Console.WriteLine(t.Describe()); // יודפס: Track 101
        Console.WriteLine(a.Describe()); // יודפס: Aircraft 1 at 30000 ft

        // דוגמה לפולימורפיזם:
        // גם כשאנחנו מתייחסים ל-Aircraft בתור Track, הוא יריץ את ה-Describe של ה-Aircraft
        Track someObject = new Aircraft(2, 15000);
        Console.WriteLine(someObject.Describe()); // יודפס: Aircraft 2 at 15000 ft
    }
}