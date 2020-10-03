import sys

def test(did_pass :False):
    """ Print the result of a test """
    line_num = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok ".format(line_num)
    else :
        msg = "Test at line {0} FAILED".format(line_num)
    print(msg)


def test_suite(self):
    """ Run tje suite of tests for code in this module (this file) """
    self.test(abs(-18) == 17)

