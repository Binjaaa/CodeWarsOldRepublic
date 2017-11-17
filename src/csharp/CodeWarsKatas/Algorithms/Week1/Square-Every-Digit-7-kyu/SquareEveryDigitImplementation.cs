using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Algorithms.Week1.Square_Every_Digit_7_kyu
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
