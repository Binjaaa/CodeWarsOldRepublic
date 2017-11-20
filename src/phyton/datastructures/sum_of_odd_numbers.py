def row_sum_odd_numbers(n):
    row_first_odd = int(0.5*(n-1)*n)
    odd_list = range(1, (row_first_odd+n)*2, 2)
    odd_row = odd_list[row_first_odd:]
    return sum(odd_row)

# Example:
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8

# print row_sum_odd_numbers(1)
# print row_sum_odd_numbers(2)
# print row_sum_odd_numbers(3)
# print row_sum_odd_numbers(4)
