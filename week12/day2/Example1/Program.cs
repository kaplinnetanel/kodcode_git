using System;

class Track
{
    public int Id { get; }
    public double Speed { get; set; }

    public Track(int id, double speed)
    {
        Id = id;
        Speed = speed;
    }
}

class Aircraft : Track // Aircraft IS-A Track
{
    public double Altitude { get; }

    public Aircraft(int id, double speed, double altitude)
        : base(id, speed) // בונה תחילה את החלק של ה-Track (הבסיס)
    {
        Altitude = altitude; // לאחר מכן את החלק הייחודי ל-Aircraft
    }
}

// דוגמה להרצה (בתוך ה-Main שלך):
class Program
{
    static void Main()
    {
        // 1. יצירת האובייקט
        Aircraft a = new Aircraft(1, 420.0, 30000.0);
   
        // 2. הדפסת שלושת הערכים
        // Id ו-Speed מגיעים מה-Base (מחלקה Track)
        // Altitude מגיע מה-Aircraft עצמו
        Console.WriteLine($"ID: {a.Id}, Speed: {a.Speed}, Altitude: {a.Altitude}");
    }
}
