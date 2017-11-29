using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class HighestLowestNumber
    {
        public static string HighAndLow(string numbers)
        {
            var nums = numbers
                .Split(' ')
                .Select(int.Parse);

            return $"{nums.Max()} {nums.Min()}";
        }
    }
}