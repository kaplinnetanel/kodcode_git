using System;

namespace exampel2;
class Example2
{
  
    static List<string> tracks = new List<string>();

    static List<double> speeds = new List<double>();

    static void AddTrack(string id, double speed) 
    {
        tracks.Add(id);
        speeds.Add(speed);
    }
                
    static double AverageSpeed() 
    {
        if (speeds.Count == 0)
        { return 0.0; }
        double sum = 0;
        foreach (double s in speeds)
        { sum += s; }
        return sum / speeds.Count;
     
    }
    static List<string> FastTracks(double threshold)
    {
        List<string> result = new List<string>();
        for (int i = 0; i < tracks.Count; i++)
        {
            if (speeds[i] > threshold)
                result.Add(tracks[i]);
        }
        return result;
   
    }
    List<string> fast = FastTracks(300);
    Console.WriteLine($"{fast.Count} fast tracks");
}

