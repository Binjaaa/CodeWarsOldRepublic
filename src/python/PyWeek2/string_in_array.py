def in_array(array1, array2):
    r = []
    for a in array1:
        for b in array2:
            if a in b:
                if a not in r:
                    r.append(a)
    r.sort()
    return r





# --------------------------------------------
# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# print in_array(a1, a2)
# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']