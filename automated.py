import os
import importlib.machinery
import subprocess
from coverage import coverage

def getName(filename):
    fn = os.path.join('test',str(filename))
    f = open(fn)
    contents = f.read()
    start = contents.find('def')
    end = contents.find('(',start)
    f.close()
    return contents[start+4:end]

    
cov = coverage()
import fnmatch
i=0
res = {}
total_failed = 0
score ={}#[1,2,3]
for file in os.listdir('test'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        str_file = str(file)
        print(str_file)
        path = os.path.join(os.getcwd(),'test')
        path = os.path.join(path,str_file)
        cov.erase()
        cov.start()
        f = file[:-3]
        loader = importlib.machinery.SourceFileLoader('mmm', path)
        mod = loader.load_module()
        funcName = getName(file)
        print(mod)
        result = getattr(mod,funcName)()
        score[i]=result
        print("result :"+str(result))
        cov.stop()
        res[i]=cov.analysis('test3.py')
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
    
        
    
    
