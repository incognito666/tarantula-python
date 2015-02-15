import os
import importlib.machinery
import subprocess
from coverage import coverage
cov = coverage()
cov.erase()
##cov.start()
#import test_a
##import test3

##import test

##print(os.getcwd())
####os.chdir('test')
##print(os.listdir())
import fnmatch
##
i=0
res = []
listmethod=['runA','runAB','runB']
for file in os.listdir():
    if fnmatch.fnmatch(file, 'test_*.py'):
        print(file)
        cov.start()
        f = file[:-3]
        ##print(f)
        loader = importlib.machinery.SourceFileLoader('mmm', file)
        mod = loader.load_module()
        ##subprocess.Popen("python "+file)
        result = getattr(mod, listmethod[i])()
        cov.stop()
        print(res)
        res=cov.analysis('test3.py')
        print(res)
        i+=1
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
##mod.runA()
####test1.runTests()
##score_a = mod.runA()
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
##score_b = mod.runB()
##cov.stop()
##results1 = cov.analysis('test3.py')
##cov.annotate()
##print(results)
##print(results1)
##cov.html_report(directory='testB')
##
##cov.erase()
##cov.start()
##score_ab=mod.runAB()
##cov.stop()
##results2=cov.analysis('test3.py')
##print(results2)
##
##calculate suspiciousness
total_failed = score_a + score_b +score_ab
total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0

print(total_failed)

susp = res[0][1]
i = 0
for x in res[0][1]:
    failed_cases = 0
    passed=0
    # for runA
    print(str(x))
    if x not in results[2]:
        if score_a == 1:
            failed_cases += 1
        else:
            passed+=1

    if x not in results1[2]:
        if score_b == 1:
            failed_cases += 1
        else:
            passed+=1
            
    if x not in results2[2]:
        if score_ab == 1:
            failed_cases += 1
        else:
            passed+=1
        
    print("failed_cases" + str(failed_cases) + " for line "+str(x))
    print("passed" + str(passed) + " for line "+str(x))
    ##passed = total_passed - failed_cases
    susp[i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
    i+=1

print(str(susp))
    
        
    
    
