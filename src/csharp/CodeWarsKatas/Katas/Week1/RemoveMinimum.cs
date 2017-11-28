using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week1
{
    public class RemoveMinimum
    {
        public static List<int> RemoveSmallest(List<int> numbers)
        {
            if (numbers == null || !numbers.Any())
                return new List<int>();

            var list = new List<int>(numbers);

            list.Remove(list.Min());
            return list;
        }
    }
}
