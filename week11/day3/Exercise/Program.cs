using System;
using System.Data;
namespace LisingStation;

class Lising
    {
                
                enum TrackClassification
                {
                    Friendly ,
                    Hostile ,
                    Unidentified
    
                }

                static bool AddSignal(List<int> ids, List<TrackClassification?> classifications, List<double?> strengths, int id, TrackClassification? classification, double? strength)
                    {
                    ids.Add(id);
                    classifications.Add(classification);
                    strengths.Add(strength);
                    return true;
                    }


                static void Calibrate(ref double? strength, double newValue)
                    {
                        strength = newValue; 
                    }

                 static void UpdateSignal(int id, List<int> ids, List<double?> strengths)
                    {
                        int? i = FindIndexById(id, ids);
                        if (i != null)
                        {
                        Console.Write("Enter new strength: ");
                        double newVal = double.Parse(Console.ReadLine());
                        Calibrate(ref strengths[i.Value], newVal);
                        }
                    }

                   static void GetAllSignal(List<int> ids, List<TrackClassification> classifications, List<double> strengths)
                    { for (int i = 0; i < ids.Count; i++) 
                        {
                            Console.Write($"id = {ids[i]},\n classification = {classifications[i]},\nstrength = {strengths[i]}");
              
                        }
    
                    }


                static int ? FindIndexById(int id , List<int> ids)
                    {for (int i = 0; i < ids.Count; i++  )
                        { if (ids[i] == id)

                            return i;
                        }
                    return null;
                    }
                 

                static void PrintMnue()
                    { Console.Write("you need to choice :\n 1.Add new signal\n 2.Update signal\n 3.GetAll signal\n 4.exit"); }
                
                

                static bool CheckInputInt(string id)
                    { 
                        if (int.TryParse(id ,out int num))
                            { return true; }
                        return false;
                    }

                static TrackClassification? CheckEnum(string number)
                       {
                          switch(number)
                            {
                                 case "1":
                                    return TrackClassification.Friendly;

                                 case "2":
                                    return TrackClassification.Hostile;

                                 case "3":
                                    return TrackClassification.Unidentified;

                                 default:
                                return null;
                             }

                        }
                static void Main()
                {
                    bool flag = true;
                    List<int> ids = new List<int>();
                    List<TrackClassification?> classifications = new List<TrackClassification?>(); 
                    List<double?> strengths = new List<double?>();

                    while (flag)
                        {
                        PrintMnue();
                        string input = Console.ReadLine();

                        if (CheckInputInt(input))
                        {
                            switch (input)
                            {
                                case "4":
                                    flag = false;
                                    break;

                                case "1":
                                    Console.Write("Enter your id? ");
                                    int number = int.Parse(Console.ReadLine());

                                    Console.Write("Enter your classification?\n 1.Friendly\n 2.Hostile \n 3.Unidentified ");
                                    TrackClassification? classification = CheckEnum(Console.ReadLine());

                                    Console.Write("Enter your strength? ");
                                    string strInput = Console.ReadLine();
                                    double? strength = double.TryParse(strInput, out double res) ? res : (double?)null;

                                    AddSignal(ids, classifications, strengths, number, classification, strength);
                                    break;

                                case "2":
                                    Console.Write("Enter ID to update: ");
                                    int updateId = int.Parse(Console.ReadLine());
                                    Console.Write("Enter new strength: ");
                                    double newVal = double.Parse(Console.ReadLine());
                                    UpdateSignal(updateId, ids, strengths, newVal);
                                    break;

                                case "3":
                                    GetAllSignal(ids, classifications, strengths);
                                    break;
                            }
                        }
                    }
                }

}




















    }