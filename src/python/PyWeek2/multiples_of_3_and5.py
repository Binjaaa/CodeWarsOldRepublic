def solution(number):
    list1 = []
    result = 0
    for i in range(1, number):
        if i not in list1 and (i % 3 == 0 or i % 5 == 0):
            list1.append(i)
            result += int(i)
    return result




#------------------------------------------------
# print solution('')
# print solution(-1)
# print solution(0)
# print solution(1)
# print solution(10)      # 3, 5, 6, 9 = 23
# print solution(16)      # 3, 5, 6, 9, 12, 15, = 60
