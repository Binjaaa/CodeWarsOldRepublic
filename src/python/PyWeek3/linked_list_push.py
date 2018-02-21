from src.python.codewars_test import test


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def push(head, data):

    pushed_head = Node(data)
    if not head:
        return pushed_head
    pushed_head.next = head
    return pushed_head

def build_one_two_three():

    data_list = [3, 2, 1]

    head = None
    for data in data_list:
        head = push(head, data)

    return head

# test.describe("tests for inserting a node before another node.")
# test.assert_equals(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
# test.assert_equals(push(None, 1).next, None, "Should be able to create a new linked list with push().")
# test.assert_equals(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
# test.assert_equals(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")
#
# test.describe("tests for building a linked list.")
# test.assert_equals(build_one_two_three().data, 1, "First node should should have 1 as data.")
# test.assert_equals(build_one_two_three().next.data, 2, "First node should should have 1 as data.")
# test.assert_equals(build_one_two_three().next.next.data, 3, "Second node should should have 2 as data.")
# test.assert_equals(build_one_two_three().next.next.next, None, "Third node should should have 3 as data.")