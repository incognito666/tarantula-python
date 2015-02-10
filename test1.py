import unittest
import test3
##import abc

##class DemoTest(unittest.TestCase):
def runTests():
    test_a()
    test_b()

def  runA():
    return test_a()

def runB():
    return test_b()

def test_a():
    try:
        assert test3.a() == True
        return 0
    except AssertionError:
        print("test_a screwed up!!")
        return 1

def test_b():
    try:
        assert test3.b() == True
        return 0
    except AssertionError:
        print("test_b screwed up!!")
        return 1


