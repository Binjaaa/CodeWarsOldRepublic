from src.python.codewars_test import test


def sum_nested(lst):
    result = 0
    lst = str(lst).replace("[", "").replace("]", "")
    for i in str(lst).split(','):
        try:
            next_number = int(i)
            result += next_number
        except:
            pass
    return result



test.describe('Should handle non-nested lists')
test.assert_equals(sum_nested([1]), 1)
test.assert_equals(sum_nested([1, 2, 3, 4]), 10)
test.assert_equals(sum_nested([1, 2, 3, 4, 8]), 18)
test.assert_equals(sum_nested(list(range(11))), 55)
test.assert_equals(sum_nested(list(range(12))), 66)
test.describe('Non-nested edge case')
test.assert_equals(sum_nested([]), 0)

test.describe('Should handle simple nestings')
test.assert_equals(sum_nested([[1], []]), 1)
test.assert_equals(sum_nested([[1, 2, 3, 4]]), 10)

test.describe('Simple nesting edge case')
test.assert_equals(sum_nested([[], []]), 0)

test.describe('Should handle more complex nestings')
test.assert_equals(sum_nested([1, [1], [[1]], [[[1]]]]), 4)
test.assert_equals(sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]), 8)

test.describe('Complex nesting edge case')
test.assert_equals(sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]), 0)