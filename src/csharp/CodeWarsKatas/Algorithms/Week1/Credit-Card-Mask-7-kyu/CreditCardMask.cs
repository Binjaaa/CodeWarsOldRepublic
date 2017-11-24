namespace CodeWarsKatas.Algorithms.Week1
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