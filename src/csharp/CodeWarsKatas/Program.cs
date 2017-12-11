using CodeWarsKatas.Katas.Week2;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CodeWarsKatas.Katas.Week4;

namespace CodeWarsKatas
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = new[,] { { 1, 3 }, { 5, 3 } };
            var b = new[,] { { 1, 2 }, { 1, 3 }, { 1, 4 } };
            var c = new int[,] { };
            var d = new[,] { { 69, 130 }, { 87, 1310 }, { 3, 4 } };

            var res = IrreducibleSumOfRationals.SumFracts(d);
            ;
        }
    }
}
