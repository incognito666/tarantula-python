import os
import importlib.machinery
import subprocess
from coverage import coverage

def getName(filename):
    f = open(filename)
    contents = f.read()
    start = contents.find('def')
    end = contents.find('(',start)
##    print(contents[start+4:end])
    f.close()
    return contents[start+4:end]

    
cov = coverage()
import fnmatch
##
i=0
res = {}
listmethod=['runA','runAB','runB']
total_failed = 0
score ={}#[1,2,3]
for file in os.listdir():
    if fnmatch.fnmatch(file, 'test_*.py'):
        print(file)
        cov.erase()
        cov.start()
        f = file[:-3]
        ##print(f)
        loader = importlib.machinery.SourceFileLoader('mmm', file)
        mod = loader.load_module()
        funcName = getName(file)
##        result = getattr(mod, listmethod[i])()
        result = getattr(mod,funcName)()
        score[i]=result
##        total_failed = total_failed+result
        print("result :"+str(result))
        cov.stop()
##        print("score: "+str(score))
        res[i]=cov.analysis('test3.py')
        print(res)
        i+=1
print("score: "+str(score))
print("res: "+str(res))

##total_failed = score_a + score_b +score_ab
for x in range(0,len(score)):
    total_failed += score[x]
total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0

print("tot failed: "+str(total_failed))
susp={}
susp = res[1]
print("susp: "+str(susp))
print("res1"+str(res[1][1]))
i = 0
for x in res[1][1]:
    failed_cases = 0
    passed=0
    # for runA
##    print(str(x))
    for y in range(1,len(res)):
        print(str(y))
        print(res[y][2])
        if x not in res[y][2]:
            if score[y] == 1:
                failed_cases+=1
            else:
                passed+=1
##
##    if x not in res[1][2]:
##        if score[0] == 1:
##            failed_cases += 1
##        else:
##            passed+=1
##
##    if x not in res[1][2]:
##        if score[1] == 1:
##            failed_cases += 1
##        else:
##            passed+=1
##            
##    if x not in res[2]:
##        if score[2] == 1:
##            failed_cases += 1
##        else:
##            passed+=1
        
        print("failed_cases" + str(failed_cases) + " for line "+str(x))
        print("passed" + str(passed) + " for line "+str(x))
    ##passed = total_passed - failed_cases
        if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
            #or total_passed==0
            print("division by zero!!!!")
        else :
            
            susp[i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
    i+=1

print(str(susp))
    
        
    
    
