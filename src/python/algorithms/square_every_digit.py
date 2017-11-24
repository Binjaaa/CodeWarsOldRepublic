def square_digits(num):
    digits_list = list(str(num))
    squared_list = list((int(i)**2 for i in digits_list))
    joined_numbers = int(''.join(str(i) for i in squared_list))
    return joined_numbers


# print square_digits(22)
# print square_digits(99)

# Example:
# For example, if we run 9119 through the function, 811181 will come out.