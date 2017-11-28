using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class HighestLowestNumber
    {
        public static string HighAndLow(string numbers)
        {
            var nums = numbers
                .Split(' ')
                .Select(n => int.Parse(n));

            return $"{nums.Max()} {nums.Min()}";
        }
    }
}