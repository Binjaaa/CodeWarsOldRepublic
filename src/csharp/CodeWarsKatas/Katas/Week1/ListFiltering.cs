using System;
using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week1
{
    internal class ListFiltering
    {
        /// <summary>
        /// In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
        /// </summary>
        /// <param name="listOfItems"></param>
        /// <returns></returns>
        public static IEnumerable<int> GetIntegersFromList(List<object> listOfItems)
        {
            return listOfItems
                .Where(x => x is int)
                .Select(Convert.ToInt32);
        }
    }
}
