biggest = max(3,7,2,5)
x = abs(3 - 11)+10
print(biggest,x)

def find_first_2_letter_word(xs):
    """print the first characters of given word"""
    for wd in xs:
        if len(wd) == 2:
            return wd;

    return ""


print(find_first_2_letter_word(["This","is","a","dead","parrot"]))