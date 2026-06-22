using System;
using System.Collections.Generic;


namespace progectDay2
{
    class ManagementConsole
    {
        
        static void AddTrack(int id, double speed, double heading,List<double> headings, List<double> speeds, List<int> ids)
        {
            ids.Add(id);
            speeds.Add(speed);
            headings.Add(heading);
        }

        static bool RemoveTrack(int id ,List<double> headings, List<double> speeds, List<int> ids)
        {

            for (int i = 0; i < ids.Count; i++) 
            { 
                if (ids[i] == id)
                {
                    ids.RemoveAt(i);
                    speeds.RemoveAt(i);
                    headings.RemoveAt(i);
                    return true;
                }
            }
            return false;
        }

        static string FindATrackById(int id, List<double> headings, List<double> speeds, List<int> ids)
        {
            for(int i = 0; i < ids.Count; i++ )
            { 
                if (ids[i] == id)
                {
                    int ide = ids[i];
                    double speed = speeds[i];
                    double heading = headings[i];
                return $"id = {ide}, speed = {speed},heading = {heading}";
                }
        
            }
            return $"not fuond id = {id} in the tracks";    
        }
        
        static void ListAllTracks(List<double> headings, List<double> speeds, List<int> ids)
        {
            for (int i = 0; i < ids.Count; i ++)
            {
               Console.WriteLine($"id = {ids[i]}");
               Console.WriteLine($"speeds = {speeds[i]}");
               Console.WriteLine($"heading = {headings[i]}");
            }
        }

        static List<int> FilterTracks(double speed, List<double> speeds, List<int> ids)
        {
            List<int> tracks = new List<int>();
            for (int i = 0; i < ids.Count; i++)
            { 
                if (speeds[i] == speed)
                {
                    tracks.Add(ids[i]);
                }
            }
            return tracks;
        
        }

        static void FilterTracks(List<int> tracks)
        {
            for (int i = 0 ; i < tracks.Count; i++)
            {
                Console.WriteLine(tracks[i]);
            }   
        }


        static string SummarizeTheFleet(List<double> speeds, List<int> ids)
            {
                int count = ids.Count;
                double sum = 0;
                double max_spid = 0; 
                
                for (int i = 0; i < count; i++)
                {
                    sum = sum + speeds[i];
                    if (max_spid < speeds[i])
                        {
                            max_spid = speeds[i];
                        }
                                                                        
                }
                return $" count = {count} , averageSpeed = {sum / count}, fastrstTrack = {max_spid}";

            }
           

        static void Main()
        {
            List<int> ids = new List<int>();
            List<double> speeds = new List<double>();
            List<double> headings = new List<double>();

            bool flag = true;
            while (flag)
            {
                Console.Write("you need to choice\n 1 Add Track\n 2 Remove Track\n 3 FindA Track By Id\n 4 List All Tracks\n 5 Filter Tracks\n 6 Summarize The Fleet\n 7 exit");
                Console.Write("Enter speed: ");
                int choice = int.Parse(Console.ReadLine());
                if (choice == 7)
                    {flag = false;}
                if (choice == 1)
                {
                    Console.Write("Enter your id: ");
                    int id = int.Parse(Console.ReadLine()); 

                    Console.Write("Enter your speed: ");
                    double speed = double.Parse(Console.ReadLine());

                    Console.Write("Enter your heading: ");
                    double heading = double.Parse(Console.ReadLine()); 

                    AddTrack(id, speed, heading, headings, speeds, ids);
                }
               
                else if (choice == 2)
                {
                    Console.Write("Enter your id");
                    int id = int.Parse(Console.ReadLine());
                    RemoveTrack(id, headings, speeds, ids);
                }
                else if (choice == 3)
                {

                    Console.Write("Enter your id");
                    int id = int.Parse(Console.ReadLine());
                    Console.WriteLine(FindATrackById(id, headings, speeds, ids));
                }
                else if (choice == 4) ListAllTracks(headings, speeds, ids);

                else if (choice == 5)
                {
                    Console.Write("Enter your speed: ");
                    double speed = double.Parse(Console.ReadLine());
                    List<int> filteredIds = FilterTracks(speed, speeds, ids);
                    FilterTracks(filteredIds);
                }
                else if (choice == 6) Console.WriteLine(SummarizeTheFleet(speeds, ids));



            }

        }

    
    }

}

    