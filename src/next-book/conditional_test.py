import math
x = -1
if x < 0:
    print('The negative number',x,'is not valid here')
    x = 42

print('The square root of',x,'is',math.sqrt(x))

def print_square_root(x):
    if x <= 0:
        print("Positive number only,Please")
        return
    result = x**0.5
    print("the square root of",x,"is ",result)

print_square_root(3)

