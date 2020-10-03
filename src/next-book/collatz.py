
def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1
    """

    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=".\n")


def tables(n):
    """ create tables"""
    for i in range(n):
        print(i, "\t", 2**i)


tables(13)
