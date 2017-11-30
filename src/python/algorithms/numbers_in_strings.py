import re


def solve(s):
    regex_group = re.compile('\d+')
    numbers_list = regex_group.findall(s)
    int_list = (int(i) for i in numbers_list)
    return max(int_list)


# print solve("12i13")
# print solve("gh12cdy695m1")
# print solve("vih61w8oohj5")

# Example:
# For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.
# https://www.codewars.com/kata/numbers-in-strings
