def high_and_low(numbers):
    numbers1 = [int(n) for n in numbers.split()]
    list1 = str(max(numbers1)) + " " + str(min(numbers1))
    return list1






# ----------------------------------------------
# print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") #  "542 -214");
# print high_and_low("1 -1") #  "1 -1");
# print high_and_low("1 1") #  "1 1");
# print high_and_low("-1 -1") #  "-1 -1");
# print high_and_low("1 -1 0") #  "1 -1");
# print high_and_low("1 1 0") #  "1 0");
# print high_and_low("-1 -1 0") #  "0 -1");
# print high_and_low("42") #  "42 42");
