import os
import importlib
import subprocess
from modulefinder import ModuleFinder
import figleaf
from importlib import import_module
import imp

def getName(filename):
    f = open(filename)
    contents = f.read()
    start = contents.find('def')
    end = contents.find('(',start)
    f.close()
    return contents[start+4:end]

    
##cov = coverage()
import fnmatch
i=0
res = {}
total_failed = 0
score ={}#[1,2,3]
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        print(file)
	figleaf.get_trace_obj();
        figleaf.start()
        f = file[:-3]
	mod=importlib.import_module(f)
        funcName = getName(file)
        result = getattr(mod,funcName)()
        score[i]=result
        print("result :"+str(result))
        figleaf.stop()
        res[i]=figleaf.get_info('test3.py')
#	res[i]=figleaf.annotate_coverage('test3.py')
#	figleaf.stop()
        print(res)
        i+=1
print("score: "+str(score))
print("res: "+str(res))
print("---------------------------------------")
for x in range(0,len(score)):
    total_failed += score[x]
total_tests = len(res)
print("Total tests: " + str(total_tests))
total_passed = total_tests - total_failed
passed = 0

print("total failed: "+str(total_failed))
##susp=[]
susp = res[0][1]
print("susp: "+str(susp))
print("res1"+str(res[1][1]))
i = 0
for x in res[1][1]:
    failed_cases = 0
    passed=0
    for y in range(0,total_tests):
        print("y is "+str(y))
        print(res[y][2])
        if x not in res[y][2]:
            if score[y] == 1:
                failed_cases+=1
            else:
                passed+=1
            
    print("failed_cases: " + str(failed_cases) + " for line "+str(x))
    print("passed: " + str(passed) + " for line "+str(x))
    ##passed = total_passed - failed_cases
    if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
        print("division by zero!!!!")
    else :
        susp[i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
    i+=1

print(str(susp))
    
        
    
    
