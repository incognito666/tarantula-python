import sys
import unittest
import os

p = os.path.join(os.getcwd(),'src')
print("@@@@@@@@@@@@@@@")
print(p)
sys.path.insert(0,p)
import test3
import test4
##import abc

##class DemoTest(unittest.TestCase):

##def runA():
##    print(os.getcwd())
##    return test_a()




def test_a():
    try:
        assert test3.a() == True
        return 0
    except AssertionError:
        print("test_a screwed up!!")
        return 1

def test_a_copy():
    try:
        assert test3.a() == True
        return 0
    except AssertionError:
        print("test_a screwed up!!")
        return 1

def test_c():
    try:
        num = 6
        print("in test_c :",test4.c(6))
        assert test4.c(6) == 6
        return 0
    except:
        print("test_c screwed up")
        return 1



