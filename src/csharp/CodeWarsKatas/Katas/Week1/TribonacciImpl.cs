using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week1
{
    internal class TribonacciImpl
    {
        public static double[] Tribonacci(double[] signature, int n)
        {
            if (n == 0)
                return new double[] { 0 };

            if (n <= signature.Length)
                return signature
                    .Take(n)
                    .ToArray();

            var list = new List<double>(signature);

            for (int i = signature.Length; i < n; i++)
            {
                list.Add(list[i - 3] + list[i - 2] + list[i - 1]);
            }

            return list.ToArray();
        }
    }
}
