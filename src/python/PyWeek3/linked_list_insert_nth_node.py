from src.python.PyWeek3.linked_list_push import build_one_two_three
from src.python.codewars_test import test


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert_nth(head, index, data):
    if index == 0:
        head = Node(data, head)

    else:
        head.next = insert_nth(head.next, index-1, data)

    if not head:
        raise IndexError
    return head


# Test
# test.it("should be able to handle an empty list.")
# test.assert_equals(insert_nth(None, 0, 12).data, 12, "should be able to insert a node on an empty/None list.")
# test.assert_equals(insert_nth(None, 0, 12).next, None, "value at index 1 should be None.")
#
# test.it("should be able to insert a new node at the head of a list.")
# test.assert_equals(insert_nth(build_one_two_three(), 0, 23).data, 23, "should be able to insert new node at head of list.")
# test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.data, 1, "value for node at index 1 should be 1.")
# test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.data, 2, "value for node at index 2 should be 2.")
# test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
# test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.next, None, "value at index 4 should be None.")
#
# test.it("should be able to insert a new node at index 1 of a list.")
# test.assert_equals(insert_nth(build_one_two_three(), 1, 23).data, 1, "value for node at index 0 should be 1.")
# test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.data, 23, "value for node at index 1 should be 23")
# test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.data, 2, "value for node at index 2 should be 2.")
# test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
# test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.next, None, "value at index 4 should be None.")
#
# test.it("should be able to insert a new node at index 2 of a list.")
# test.assert_equals(insert_nth(build_one_two_three(), 2, 23).data, 1, "head should remain unchanged after inserting new node at index 2")
# test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at index 2")
# test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.data, 23, "value for node at index 2 should be 23.")
# test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
# test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.next, None, "value at index 4 should be None.")
#
# test.it("should be able to insert a new node at tail of a list.")
# test.assert_equals(insert_nth(build_one_two_three(), 3, 23).data, 1, "head should remain unchanged after inserting new node at tail")
# test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at tail")
# test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.data, 3, "value for node at index 2 should be 3.")
# test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.data, 23, "value for node at index 3 should be 23.")
# test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.next, None, "value at index 4 should be None.")
#
# test.it("should raise exception if index is too large.")
# test.expect_error("Invalid index value should raise error.", lambda : insert_nth(build_one_two_three(), 4, 23))