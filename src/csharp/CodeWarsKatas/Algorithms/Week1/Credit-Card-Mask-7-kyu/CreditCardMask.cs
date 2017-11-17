using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Algorithms.Week1.Credit_Card_Mask_7_kyu
{
    internal class CreditCardMask
    {
        public static string Maskify(string str)
        {
            if (string.IsNullOrWhiteSpace(str))
                return string.Empty;

            var length = str.Length;

            if (length > 4)
            {
                var visibleStartIndex = length - 4;
                var secretPart = new string('#', visibleStartIndex);
                var visiblePart = str.Substring(visibleStartIndex);
                return $"{secretPart}{visiblePart}";
            }

            return str;
        }
    }
}
