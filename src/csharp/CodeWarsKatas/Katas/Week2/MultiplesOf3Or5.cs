using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class MultiplesOf3Or5
    {
        public static int ThreeOrFiveMultiples(int n)
        {
            return Enumerable.Range(0, n)
                .Where(x => x % 3 == 0 || x % 5 == 0)
                .Sum();
        }
    }
}