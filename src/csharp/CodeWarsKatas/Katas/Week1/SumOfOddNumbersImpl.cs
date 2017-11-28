using System.Linq;
using System.Text.RegularExpressions;

namespace  CodeWarsKatas.Katas.Weel1
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