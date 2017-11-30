def high_and_low(numbers):
    splitNumbers = [int(n) for n in numbers.split()]
    return str(max(splitNumbers)) + " " + str(min(splitNumbers))






# ----------------------------------------------
# print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") #  "542 -214");
# print high_and_low("1 -1") #  "1 -1");
# print high_and_low("1 1") #  "1 1");
# print high_and_low("-1 -1") #  "-1 -1");
# print high_and_low("1 -1 0") #  "1 -1");
# print high_and_low("1 1 0") #  "1 0");
# print high_and_low("-1 -1 0") #  "0 -1");
# print high_and_low("42") #  "42 42");
