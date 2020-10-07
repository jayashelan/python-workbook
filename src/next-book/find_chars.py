def find(strng,ch):
    """ Find and return the index of ch in string
    Return -1 if ch does not occur in string"""
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix;
        ix += 1
    return -1


print(find("compsci","p"))
print(find("compsci","c"))

