using System;
namespace Example1;

class example
    {
     static void TryDouble(int n) { n = n * 2; } // n is a copy
     static void AddOne(List<int> xs) { xs.Add(1); } // xs points to the sam list

    static bool FindSpeed(string id, out double speed)
    {
        speed = 0; // out parameters must be set befor returning
        if (id == "TR-1") { speed = 420.5; return true; }
            return false;
    }



    enum TrackStatus { Active, Lost, Intercepted }

    static void Hobule()
    {

        TrackStatus st = TrackStatus.Active;
        Console.WriteLine(st);
        if (st == TrackStatus.Active)
            Console.WriteLine("track is active");

    }

    static void Main()
    {

        double? speed = null; // radar has not locked — trul unknown
        Console.WriteLine(speed.HasValue); // False
        Console.WriteLine(speed ?? -1); // -1 stands in for unknown when printing
        speed = 412.5; // now the radar locked
        Console.WriteLine(speed.HasValue); // True
        Console.WriteLine(speed.Value);


        Hobule();
        int x = 10;
        TryDouble(x);
        Console.WriteLine(x); // 10 — the int was copied, calle unchanged
        List<int> list = new List<int>();
        AddOne(list);
        Console.WriteLine(list.Count); // 1 — the list is shared, caller sees th change
        if (FindSpeed("TR-1", out double s))
            Console.WriteLine($"found: {s}");

        else
            Console.WriteLine("not found");
        
    }
    




}


