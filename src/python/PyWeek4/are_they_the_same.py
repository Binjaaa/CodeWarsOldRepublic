from src.python.codewars_test import test


def comp(array1, array2):
    array1_sq = []

    for i in array1:
        array1_sq.append(i**2)
    if array1_sq:
        array1_sq.sort()
    if array2:
        array2.sort()

    return array1_sq == array2

# Test
# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
# test.assert_equals(comp(a1, a2), True)