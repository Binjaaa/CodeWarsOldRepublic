using System.Linq;
using System.Text.RegularExpressions;

namespace CodeWarsKatas.Katas.Week4
{
    internal class PascalCaseToSnake
    {
        public static string ToUnderscore(int str)
        {
            return str.ToString();
        }

        public static string ToUnderscore(string str)
        {
            var query = str.Select((c, i) =>
            {
                if (i == 0)
                    return char.ToLowerInvariant(c).ToString();

                return char.IsUpper(c)
                    ? $"_{char.ToLowerInvariant(c)}"
                    : c.ToString();
            });

            return string.Join("", query);
        }

        public static string ToUnderscore2(string str)
        {
            var subPart = Regex
                .Replace(str, @"\B[A-Z]", m => $"_{m.ToString().ToLower()}")
                .Substring(1);

            return char.ToLowerInvariant(str[0]) + subPart;
        }
    }
}