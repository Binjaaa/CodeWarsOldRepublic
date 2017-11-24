def delete_nth(order, max_e):
    list1 = []
    for i in order:
        if list1.count(i) < max_e:
            list1.append(i)
    print list1



# ----------------------------------------------------------------------
delete_nth([20, 37, 20, 21], 1) # , [20, 37, 21]
delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) # , [1, 1, 3, 3, 7, 2, 2, 2]