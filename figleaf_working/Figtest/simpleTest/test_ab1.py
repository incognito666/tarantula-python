import unittest
import test3

##def runAB():
##    return test_a_b()

def test_a_b():
    try:
        assert test3.b() == False and test3.a() == True
        return 0
    except AssertionError:
        print("test_a_b screwed up!!")
        return 1
