import unittest
import src.test3

def runB():
    return test_b()



def test_b():
    try:
        assert test3.b() == True
        return 0
    except AssertionError:
        print("test_b screwed up!!")
        return 1
