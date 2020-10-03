import test1


def my_sum(xs):
    """ Sum all the numbers in the list xs and return the total"""
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total



# Add test like these to your test suite ....
test1.test(my_sum([2, 3, 4, 6]) == 15)
