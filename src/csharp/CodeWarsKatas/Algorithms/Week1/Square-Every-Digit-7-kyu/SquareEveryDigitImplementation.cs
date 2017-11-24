using System;
using System.Linq;

namespace CodeWarsKatas.Algorithms.Week1
{
    internal class SquareEveryDigitImplementation
    {
        public static int SquareEveryDigit(int n)
        {
            var newNumber = n
                .ToString()
                .Select(c => Math.Pow(char.GetNumericValue(c), 2));

            return Convert.ToInt32(string.Join("", newNumber));
        }
    }
}