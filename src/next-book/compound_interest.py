
def final_amt(p,r,n,t):
    """
    Apply the compound interest formula to p to produce the final amount
    """
    a = p * (1 + r/n) ** (n*t)
    return a

def final_amt_v3(amt,rate,compound,years):
    a = amt * ( 1 + rate/compound) ** (compound * years)
    return a
# call the function
toInvest = float(1000.0)
fnl = final_amt_v3(toInvest,0.08,12,5)
print("At the end of the period you'll have",fnl)

