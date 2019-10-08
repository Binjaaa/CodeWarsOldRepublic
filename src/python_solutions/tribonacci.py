def tribonacci(signature, n):
    len_sig = len(signature)
    trib_list = signature

    if n <= 3:
        return trib_list[:n]

    for i in range(0, n-len_sig):
        trib_list.append(trib_list[i] + trib_list[i+1] + trib_list[i+2])
    return trib_list




print(tribonacci([1, 1, 1], 0))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([1, 1, 1], 2))
# print tribonacci([0, 0, 1], 10)
# print tribonacci([1, 0, 0], 10)
# print tribonacci([1, 2, 3], 10)

# https://www.codewars.com/kata/tribonacci-sequence

# Test.describe("Basic tests")
# Test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
# Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
# Test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
# Test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
# Test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# Test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
# Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
# Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
# Test.assert_equals(tribonacci([300, 200, 100], 0), [])
# Test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30),
#                    [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5,
#                     3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5,
#                     1655616.5, 3045153.5, 5600910.5, 10301680.5])