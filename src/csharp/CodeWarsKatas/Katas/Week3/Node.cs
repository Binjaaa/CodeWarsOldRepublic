using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeWarsKatas.Katas.Week3
{
    public class Node
    {
        public int Data;
        public Node Next;

        public Node(int data)
        {
            this.Data = data;
            this.Next = null;
        }

        public static Node Push(Node head, int data)
        {
            var newHead = new Node(data);

            if (head == null)
                return newHead;

            newHead.Next = head;

            return newHead;
        }

        public static int Length(Node head)
        {
            if (head == null)
                return 0;

            return head.Next == null ? 1 : Length(head.Next) + 1;
        }

        public static int Count(Node head, Predicate<int> func)
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

        public static Node BuildOneTwoThree()
        {
            var n2 = Push(new Node(3), 2);

            return Push(n2, 1);
        }

        public static Node InsertNth(Node head, int index, int data)
        {
            if (head == null)
                return new Node(data);

            if (index == 0)
                return new Node(data) { Next = head };

            if (index < 0 || index > Length(head))
                throw new ArgumentOutOfRangeException(nameof(index));

            var i = 0;
            var currentNode = head;

            while (i++ != index - 1)
            {
                currentNode = currentNode.Next;
            }

            currentNode.Next = new Node(data) { Next = currentNode.Next };


            return head;
        }

        public static Node GetNth(Node node, int index)
        {
            if (node == null || Length(node) == 0)
                throw new ArgumentException(nameof(node));

            if (index < 0 || index >= Length(node))
                throw new ArgumentException(nameof(index));

            var i = 0;
            var currentNode = node;

            while (i++ <= index - 1)
            {
                currentNode = currentNode.Next;
            }

            return currentNode;
        }


        public static string Stringify(Node list)
        {
            return list == null 
                ? "null" 
                : $"{list.Data} -> " + Stringify(list?.Next);
        }
    }
}
