def group_check(s):
    brackets = ['(', ')', '[', ']', '{', '}']
    pairs = ['()', '[]', '{}']
    list1 = []
    j = 0
    for i in range(len(s)):
        if s[i] in brackets:
            list1.append(s[i])
    string_brackets = ''.join(list1)
    while len(string_brackets) > 0 and ('{}' in string_brackets or '[]' in string_brackets or '()' in string_brackets):
        current_pair = pairs[j]
        if current_pair in string_brackets and j < 3:
            string_brackets = string_brackets.replace(current_pair,'')
            print(string_bracketsw)
            j = 0
        else:
            j += 1

    return len(string_brackets) <= 0

# group_check("")
print(group_check("{([{(123)[456]}])}[]"))