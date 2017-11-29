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

            if (index < 0 || index > head.Length())
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
    }
}
