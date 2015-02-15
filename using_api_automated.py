import os
import importlib.machinery
from coverage import coverage
cov = coverage()
cov.erase()
cov.start()
#import test_a
##import test3

##import test

##print(os.getcwd())
####os.chdir('test')
##print(os.listdir())
import fnmatch
##

for file in os.listdir():
    if fnmatch.fnmatch(file, 'test_*.py'):
        print(file)
##        f = file[:-3]
        ##print(f)
        loader = importlib.machinery.SourceFileLoader('mmm', file)
        mod = loader.load_module()
        print(mod)
####        globals[f] = __import__(f)
##import 

##from test import test_a
##test.test_a.runA()
##list1 = ['test_a.py','test_b']#'test_a.py'
##loader = importlib.machinery.SourceFileLoader('mmm', list1)
##mod = loader.load_module()
##print(mod)
##modules=map(__import__,list1)
##importlib.import_module(list1)
##print(x[2])
mod.runA()
##test1.runTests()
##score_a = test1.runA()
##
##
##
##
##
##cov.stop()
##results = cov.analysis('test3.py')
##cov.annotate('test3.py')
##cov.html_report(directory='testA')
##cov.erase()
##
##cov.start()
##score_b = test1.runB()
##cov.stop()
##results1 = cov.analysis('test3.py')
##cov.annotate()
##print(results)
##print(results1)
##cov.html_report(directory='testB')
##
##cov.erase()
##cov.start()
##score_ab=test1.runAB()
##cov.stop()
##results2=cov.analysis('test3.py')
##print(results2)
##
####calculate suspiciousness
##total_failed = score_a + score_b +score_ab
##total_tests = 3
##total_passed = total_tests - total_failed
##passed = 0

##print(total_failed)
##
##susp = results[1]
##i = 0
##for x in results[1]:
##    failed_cases = 0
##    passed=0
##    # for runA
##    print(str(x))
##    if x not in results[2]:
##        if score_a == 1:
##            failed_cases += 1
##        else:
##            passed+=1
##
##    if x not in results1[2]:
##        if score_b == 1:
##            failed_cases += 1
##        else:
##            passed+=1
##            
##    if x not in results2[2]:
##        if score_ab == 1:
##            failed_cases += 1
##        else:
##            passed+=1
##        
##    print("failed_cases" + str(failed_cases) + " for line "+str(x))
##    print("passed" + str(passed) + " for line "+str(x))
##    ##passed = total_passed - failed_cases
##    susp[i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
##    i+=1
##
##print(str(susp))
    
        
    
    
