using System;

namespace SingelTrack
{
    class TrackManagement
    {
        static void Main()
        {
            bool flag = true;
            while (flag)
            {
                Console.Write("what trackId?");
                string id = Console.ReadLine();

                Console.Write("what your speed?");
                string speed = Console.ReadLine();

                Console.Write("what your Heading:");
                string heading = Console.ReadLine();

                Console.Write("what your status:");
                string status = Console.ReadLine();

                int trackId;
                double trackSpeed;
                double trackHeading;
                string category = "";

                if (int.TryParse(id, out trackId))
                { }
                else
                {
                    Console.WriteLine("id not type int");
                    break;
                }
                if (double.TryParse(speed, out trackSpeed))
                {
                    if (trackSpeed < 100)
                    {
                        category = "slow";
                    }
                    else if (trackSpeed <= 300)
                    {
                        category = "medium";
                    }
                    else category = "fast";
                }
                else
                {
                    Console.WriteLine("sped need type int");
                    break;
                }
                if (double.TryParse(heading, out trackHeading))
                {
                    if (trackHeading >= 0 && trackHeading <= 359)
                    { }
                    else
                    {
                        Console.WriteLine("heading neeed between 0 =< trackHeading <= 359 ");
                        break;
                    }
                }
                else
                {
                    Console.WriteLine("heading need type double");
                    break;
                }
                if (status == "cruising" || status == "turning" || status == "stopped" || status == "accelerating")
                { }
                else
                {
                    Console.WriteLine("status need in (cruising, turning, stopped, accelerating)");
                    break;
                }

                Console.WriteLine("\n=== Track Report ===");
                Console.WriteLine($"Track ID: {trackId}");
                Console.WriteLine($"Speed: {trackSpeed} km/h ({category})");
                Console.WriteLine($"Heading: {trackHeading} degrees");
                Console.WriteLine($"Status: {status}");
                Console.WriteLine($"Division Demo 1: {trackId}/10 = {trackId / 10} (int) | {trackId / 10.0} (double)");
                Console.WriteLine($"Division Demo 2: {trackSpeed}/60 = {(int)trackSpeed / 60} (int) | {trackSpeed / 60.0} (double)");

                flag = false;
            }
        }
    }
}