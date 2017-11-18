using System;
using System.Linq;

namespace CodeWarsKatas.Algorithms.Week1
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