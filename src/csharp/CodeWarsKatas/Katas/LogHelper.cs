using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Katas
{
    internal static class LogHelper
    {
        internal static string Log(int[] array)
        {
            return array == null
                ? "[null]"
                : array.Any() ? string.Join(",", array.Select(x => $"\"{x}\"")) : "[empty]";
        }

        internal static IEnumerable<string> Log(int[,] array2D)
        {
            for (var i = 0; i < array2D.GetLength(0); i++)
            {
                for (var j = 0; j < array2D.GetLength(1); j++)
                {
                    yield return array2D[i, j].ToString();
                }
            }
        }

        internal static void LogConsole(IEnumerable<string> strs)
        {
            Console.WriteLine(string.Join(",", strs));
        }
    }
}
