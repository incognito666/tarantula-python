import unittest
import os
import test3
##import abc

##class DemoTest(unittest.TestCase):

def runA():
    print(os.getcwd())
    return test_a()




def test_a():
    try:
        assert test3.a() == True
        return 0
    except AssertionError:
        print("test_a screwed up!!")
        return 1




