from src.python.PyWeek3.linked_list_insert_nth_node import Node
from src.python.codewars_test import test

def stringify(node):
    result = ""
    while node:
        data = node.data
        result += str(data) + " -> "
        node = node.next
    return result + "None"

# ---------------------------------
# test.describe("stringify()")
#
# test.it("should pass the example tests as shown in the Description")
# test.assert_equals(stringify(Node(0, Node(1, Node(2, Node(3))))), '0 -> 1 -> 2 -> 3 -> None')
# test.assert_equals(stringify(Node(0, Node(1, Node(2, Node(3))))), '0 -> 1 -> 2 -> 3 -> None')
# test.assert_equals(stringify(None), 'None')
# test.assert_equals(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))), '0 -> 1 -> 4 -> 9 -> 16 -> None')