# newtons fornula -> better= (approx + n/approx) /2

def sqrt(n):
    """ use newtons formula better = (approx + n/approx) /2"""
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        if(abs(approx - better)) < 0.001:
           return better
        approx = better

# Test Cases:
print(sqrt(3.0))

