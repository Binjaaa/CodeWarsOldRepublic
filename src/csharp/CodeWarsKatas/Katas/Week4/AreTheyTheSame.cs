using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Katas.Week4
{
    internal class AreTheyTheSame
    {
        /* 
          a = [121, 144, 19, 161, 19, 144, 19, 11]  
          b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        */

        public static bool Comp(int[] a, int[] b)
        {
            if (a == null || b == null)
                return false;

            if (a.Length == 0 && b.Length == 0)
                return true;

            if (a.Length != b.Length)
                return false;

            var squares = a
                .Select(x => x * x)
                .Count(b.Contains);

            var hh = a
                .Select(x => x * x)
                .Where(b.Contains)
                .ToList();




            //var countT = 0;
            //foreach (int i in b)
            //{
            //    var check = false;
            //    if (a.Any(j => Math.Sqrt(i) == j))
            //    {
            //        check = true;
            //        countT++;
            //    }

            //    if (check == false)
            //        return false;
            //}
            //return countT == b.Length ? true : false;

            return squares == b.Length;
        }
    }
}
