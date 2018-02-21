from src.python.PyWeek3.linked_list_push import build_one_two_three

def get_nth(node, index):
    if not node or index < 0:
        raise IndexError
    for i in range(index):
        node = node.next
        if not node:
            raise IndexError
    return node




#  Test
# list = build_one_two_three()
# print list
# print get_nth(list, 0).data #, 1, "First node should be located at index 0."
# print get_nth(list, 1).data #, 2, "Second node should be located at index 1."
# print get_nth(list, 2).data #, 3, "Third node should be located at index 2."
# try:
#     print get_nth(list, 3) # ("Invalid index value should throw error.")
# except: print "Error"
# try:
#     print get_nth(list, -1) # ("Invalid index value should throw error.")
# except: print "Error"
# try:
#     print get_nth(list, 100) # ("Invalid index value should throw error.")
# except: print "Error"
# try:
#     print get_nth(None, 0) # ("None linked list should throw error.")
# except: print "Error"