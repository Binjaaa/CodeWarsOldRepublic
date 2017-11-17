using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Algorithms.Week1.Find_the_next_perfect_square__7_kyu
{
    internal class NextPerfectSquare
    {
        public static long NextPerfectSqrt(long num)
        {
            return new[] { (long)Math.Sqrt(num) }
                .Select(sqrt =>
                {
                    var perfectSqrt = sqrt * sqrt;
                    var nextSqrtBase = sqrt + 1;

                    return num == perfectSqrt ? nextSqrtBase * nextSqrtBase : -1;
                })
                .First();
        }
    }
}
