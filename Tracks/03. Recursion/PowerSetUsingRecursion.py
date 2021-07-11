# Rest of the code is already given

def powerSet(s):
    perm = []
    if len(s) == 0:
        perm.append("")
        return perm
    first = s[0]
    rem = s[1:len(s)]
    words = powerSet(rem)
    perm.extend(words)
    for word in words:
        perm.append(first+word)
    return perm