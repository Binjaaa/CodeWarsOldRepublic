def order_weight(strng):
    num_list = [(str(x)) for x in list(strng.split(" "))]
    dict_list = [{sum(map(int, str(x))):[x]} for x in num_list if len(x) > 0]
    result = ""
    for i in sorted(dict_list):
        for key, value in i.items():
            result += value[0] + " "
    return result[:-1]
