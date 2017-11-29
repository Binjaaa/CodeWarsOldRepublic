using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CodeWarsKatas.Katas.Week3
{
    public static class NodeMethods
    {
        /// <summary>
        /// Push method with extension method for a cleaner solution
        /// Example: new Node(1).Push(2).Push(3)
        /// </summary>
        /// <param name="node"></param>
        /// <param name="index"></param>
        /// <returns></returns>
        //public static Node Push(this Node head, int data)
        //{
        //    var newHead = new Node(data);

        //    if (head == null)
        //        return newHead;

        //    newHead.Next = head;

        //    return newHead;
        //}

        public static Node GetNth(this Node node, int index)
        {
            return null;
        }

        public static int Length(this Node head)
        {
            if (head == null)
                return 0;

            return head.Next == null ? 1 : Length(head.Next) + 1;
        }

        public static int Count(this Node head, Predicate<int> func)
        {
            if (head == null)
                return 0;

            var count = 0;
            var currentNode = head;

            do
            {
                if (func(currentNode.Data))
                    count++;

                currentNode = currentNode.Next;

            } while (currentNode != null);

            return count;
        }
    }
}
