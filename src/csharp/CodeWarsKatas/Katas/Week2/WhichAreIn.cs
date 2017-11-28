using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class WhichAreIn
    {
        public static string[] Which(string[] array1, string[] array2)
        {
            var words =
                from a1 in array1
                from a2 in array2
                where a2.Contains(a1)
                orderby a1
                select a1;

            return words
                .Distinct()
                .ToArray();
        }
    }
}