from src.python.PyWeek3.linked_list_push import build_one_two_three
from src.python.codewars_test import test


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def length(node):
    i = 0
    while node:
        i += 1
        node = node.next
    return i

def count(node, data):
    i = 0
    while node:
        if node.data == data:
            i += 1
        node = node.next
    return i


# Test
# test.describe("tests for counting the length of a linked list.")
# list = build_one_two_three()
# test.assert_equals(length(None), 0, "Length of null list should be zero.")
# test.assert_equals(length(Node(99)), 1, "Length of single node list should be one.")
# test.assert_equals(length(list), 3, "Length of the three node list should be three.")
#
# test.describe("tests for counting occurrences of a particular integer in a linked list.")
# list = build_one_two_three()
# test.assert_equals(count(list, 1), 1, "list should only contain one 1.")
# test.assert_equals(count(list, 2), 1, "list should only contain one 2.")
# test.assert_equals(count(list, 3), 1, "list should only contain one 3.")
# test.assert_equals(count(list, 99), 0, "list should return zero for integer not found in list.")
# test.assert_equals(count(None, 1), 0, "null list should always return count of zero.")