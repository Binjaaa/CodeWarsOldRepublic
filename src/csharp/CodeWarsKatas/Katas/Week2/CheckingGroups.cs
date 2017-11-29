using System.Collections.Generic;
using System.Linq;

namespace CodeWarsKatas.Katas.Week2
{
    internal class CheckingGroups
    {
        private static bool IsMatchingParenthesis(char c1, char c2)
        {
            if (c1 == '(' && c2 == ')')
                return true;

            if (c1 == '[' && c2 == ']')
                return true;

            if (c1 == '{' && c2 == '}')
                return true;

            return false;
        }

        public static bool Check(string input)
        {
            var stack = new Stack<char>();

            foreach (var chr in input)
            {
                if (chr == '(' || chr == '[' || chr == '{')
                    stack.Push(chr);

                if (chr == ')' || chr == ']' || chr == '}')
                {
                    if (!stack.Any())
                        return false;

                    if (!IsMatchingParenthesis(stack.Pop(), chr))
                        return false;
                }
            }

            return !stack.Any();
        }
    }
}