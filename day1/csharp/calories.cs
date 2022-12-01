using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Calories
{
    class Elf
    {
        public int calories = 0;
        public int position = 0;
    }
    class calories
    {

        static void Main()
        {
            string[] lines = System.IO.File.ReadAllLines(@"../../../input.txt");
            List<Elf> elves = new List<Elf>();
            int elfcount = 1;
            Elf currentElf = new Elf();
            currentElf.position = elfcount;
            foreach (string line in lines)
            {
                if (line != "")
                {
                    currentElf.calories += int.Parse(line);
                }
                else
                {
                    elves.Add(currentElf);
                    elfcount++;
                    currentElf = new Elf();
                    currentElf.position = elfcount;
                }
            }
            elves.Sort((a, b) => a.calories.CompareTo(b.calories));
            elves.Reverse();
            Console.WriteLine("Highest Count:" + elves.First().calories);
            Console.WriteLine("Top 3:" + elves.Take(3).Sum(a => a.calories));
            Console.ReadLine();
        }
    }
}
