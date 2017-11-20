def filter_list(l):
    list_numbers = (i for i in l if isinstance(i, (int, float)))
    return list(list_numbers)



# print filter_list([1,2,'a','b'])
# print filter_list([1,'a','b',0,15])
# print filter_list([1,2,'aasf','1','123',123])

# Example
#
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]