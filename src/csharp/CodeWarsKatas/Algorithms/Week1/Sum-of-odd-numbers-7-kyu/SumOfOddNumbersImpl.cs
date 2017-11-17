using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace CodeWarsKatas.Algorithms.Week1.Sum_of_odd_numbers_7_kyu
{
    internal class SumOfOddNumbersImpl
    {
        public static int Solve(string s)
        {
            return new Regex(@"\d+")
                .Matches(s)
                .Cast<Match>()
                .OrderByDescending(x => x.Length)
                .Select(x => int.Parse(x.Value))
                .Max();
        } 
    }
}
