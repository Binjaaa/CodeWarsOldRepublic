def accum(s):
    r = ""
    for i in range(len(s)):
        if s[i] == s[i].upper():
            r += str(s[i]) + str(s[i]*i).lower()
        else:
            r += str(s[i]).upper() + str(s[i] * i)
        if i == len(s)-1:
            return r
        r += "-"
    return r

# print accum("ZpglnRxqenU")    #
# print accum("abcd")    # "A-Bb-Ccc-Dddd"
# print accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# print accum("cwAt")    # "C-Ww-Aaa-Tttt"