import math

def distance(x1,y1,x2,y2):
    dx = x2 -x1
    dy = y2 - y1
    dsquared = dx * dx + dy * dy
    print(dsquared)
    result = dsquared ** 0.5

    return math.sqrt( (x2 -x1) ** 2 + (y2 - y1)**2)


print(distance(1,2,4,6))