from src.python.codewars_test import test


def dirReduc(myarray):
    result = ' '.join(myarray)

    while True:
        len_result = len(result)
        result = result.replace(
            'NORTH SOUTH', '').replace(
            'SOUTH NORTH', '').replace(
            'EAST WEST', '').replace(
            'WEST EAST', '')
        result = ' '.join(result.split())
        if len_result == len(result):
            return result.split()


# Test
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# print dirReduc(a)
# test.assert_equals(dirReduc(a), ['WEST'])
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
