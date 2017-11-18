def remove_smallest(numbers):
    if numbers == []:
        return numbers
    else:
        smallest_index = numbers.index(min(numbers))
        numbers.pop(smallest_index)
        return numbers


# Examples
#
# remove_smallest([1,2,3,4,5]) = [2,3,4,5]
# remove_smallest([5,3,2,1,4]) = [5,3,2,4]
# remove_smallest([2,2,1,2,1]) = [2,2,2,1]
