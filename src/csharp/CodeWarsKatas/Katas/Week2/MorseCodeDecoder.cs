using System;
using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class MorseCodeDecoder
    {
        public static string Decode(string morseCode)
        {
            var chars = morseCode
                .Trim()
                .Split(new[] { "  ", " " }, StringSplitOptions.None)
                .Select(x => string.IsNullOrEmpty(x) ? " " : MorseCode.Get(x));

            return string.Join("", chars);
        }
    }

    internal class MorseCode
    {
        public static string Get(string morse)
        {
            switch (morse)
            {
                case "....": return "H";
                case ".": return "E";
                case "-.--": return "Y";
                case ".---": return "J";
                case "..-": return "U";
                case "-..": return "D";
                default: return "";
            }
        }
    }
}