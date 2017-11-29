using System.Collections.Generic;

namespace CodeWarsKatas.Katas.Week2
{
    internal class DeleteNthOccurence
    {
        public static int[] DeleteNth(int[] arr, int x)
        {
            var occurences = new Dictionary<int, int>();
            var retVal = new List<int>();

            foreach (var element in arr)
            {
                if (occurences.ContainsKey(element))
                {
                    if (occurences[element] == x)
                        continue;

                    occurences[element]++;
                }
                else
                {
                    occurences[element] = 1;
                }

                retVal.Add(element);
            }

            return retVal.ToArray();
        }
    }
}