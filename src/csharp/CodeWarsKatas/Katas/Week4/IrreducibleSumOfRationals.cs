using System;
using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week4
{
    internal class IrreducibleSumOfRationals
    {
        private static int GreatestCommonDivisor(int a, int b)
        {
            while (a != b)
            {
                if (a > b)
                    a -= b;
                else
                    b -= a;
            }

            return a;
        }

        private static Rational SimplifyFraction(Rational rational)
        {
            var gcd = GreatestCommonDivisor(rational.N, rational.D);

            return new Rational(rational.N / gcd, rational.D / gcd);
        }

        private static int LeastCommonMultiple(int d1, int d2)
        {
            return Math.Abs(d1 * d2) / GreatestCommonDivisor(d1, d2);
        }

        private static int LeastCommonMultiple(IEnumerable<Rational> rationals)
        {
            return rationals
                .Select(r => r.D)
                .Aggregate(LeastCommonMultiple);
        }

        private static IEnumerable<Rational> SetLeastCommonMultiple(List<Rational> rationals)
        {
            Func<Rational, int, Rational> setCommonDenominator = (r, lcm) =>
                r.D != lcm
                    ? new Rational(lcm / r.D * r.N, lcm)
                    : r;

            var leastCommonMultiple = LeastCommonMultiple(rationals);

            return rationals.Select(r => setCommonDenominator(r, leastCommonMultiple));
        }

        public static string SumFracts(int[,] l)
        {
            if (l == null || l.Length == 0)
                return null;

            var fractions = Enumerable.Range(0, l.GetLength(0))
                .Select(index => SimplifyFraction(new Rational(l[index, 0], l[index, 1])));

            var res = SetLeastCommonMultiple(fractions.ToList())
                .Aggregate((r1, r2) => new Rational(r1.N + r2.N, r2.D));

            return SimplifyFraction(res).ToString();
        }

        internal struct Rational
        {
            /// <summary>
            ///     Numerator
            /// </summary>
            internal readonly int N;

            /// <summary>
            ///     Denominator
            /// </summary>
            internal readonly int D;

            internal Rational(int n, int d)
            {
                N = n;
                D = d;
            }

            public override string ToString()
            {
                return N % D == 0 ? $"{N / D}" : $"[{N}, {D}]";
            }
        }
    }
}