using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week3
{
    internal class DirectionReduction
    {
        private static bool IsReducable(string d1, string d2)
        {
            if (d1 == "SOUTH" && d2 == "NORTH")
                return true;

            if (d1 == "NORTH" && d2 == "SOUTH")
                return true;

            if (d1 == "EAST" && d2 == "WEST")
                return true;

            if (d1 == "WEST" && d2 == "EAST")
                return true;

            return false;
        }

        private static string LogHelper(string[] array)
        {
            return string.Join(",", array.Select(x => $"\"{x}\""));
        }

        public static string[] DirReduc(string[] arr)
        {
            var reducedDirections = new List<string>(arr);

            for (int i = 0; i < reducedDirections.Count - 1; i++)
            {
                if (IsReducable(arr[i], arr[i + 1]))
                {
                    reducedDirections.RemoveRange(i, 2);

                    return DirReduc(reducedDirections.ToArray());
                }
            }

            return arr;
        }
    }
}