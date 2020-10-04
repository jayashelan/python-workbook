def print_mult_table(high):
    for i in range(1,high+1):
        print_multiples(i,i+1)

def print_multiples(n,high):
    for i in range(1,high +1):
        print(n * i,end="   ")
    print()


print_mult_table(13)