import os
import importlib.machinery
import subprocess
from coverage import coverage

def getSourceFiles():
    l = []
    for f in os.listdir('src'):
        print(f)
        if os.path.isfile(os.path.join('src',f)) and f[0] is not '_':
            l.append(f)
    return l

def getNames(filename):
    names = []
    fn = os.path.join('test',str(filename))
    print(fn)
    f = open(fn)
    contents = f.readlines()
    print("func read start :")
    for line in contents:
        if not (line.strip().startswith("#")):
            start = line.find('def')
            if start != -1:
                end = line.find('(',start)
                print(line)
                names.append(line[start+4:end])
                #return line[start+4:end]
    f.close()
    #print(line[start+4:end])
    return names

    
cov = coverage()
import fnmatch
i=0
res = {} #to store the cov.analysis for each file in each test
print(os.getcwd())
source_files = getSourceFiles()
print("Src files")
print(source_files)
total_failed = 0
score ={}#[1,2,3]
for file in os.listdir('test'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        all_files = {}
        str_file = str(file)
        print(str_file)
        path = os.path.join(os.getcwd(),'test')
        path = os.path.join(path,str_file)
        cov.erase()
        cov.start()
        f = file[:-3]
        loader = importlib.machinery.SourceFileLoader('mmm', path)
        mod = loader.load_module()
        funcNames = getNames(file)
        #print(mod)
        for funcName in funcNames:
            if funcName  != "":
                print(funcName)
                result = getattr(mod,funcName)()
        score[i]=result
        print("result :"+str(result))
        cov.stop()
        print("**************************")
        for single_file in source_files:
            all_files[single_file] = cov.analysis("src/"+single_file)
        res[i]=all_files
        print(res[i])
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
## to handle multiple src files, susp will now be a dict
## with key as filename in /src folder and value as it's susp value
susp = {}

for single_file in source_files:
    susp[single_file] = res[0][single_file][1]

print("Susp", susp)
##susp = res[0][1]
all_executable_lines = susp
##print("susp: "+str(susp))
##print("res1"+str(res[1][1]))
## for each file in source_files calc suspiciousness

for single_file in source_files:
    print("for ",single_file)
    print(all_executable_lines[single_file])
    i = 0
    for x in all_executable_lines[single_file]: ## to get executable lines for that file
        print("Exec line ",x)
        failed_cases = 0
        passed=0
        for y in range(0,total_tests):
            print("y is "+str(y))
            print(res[y][single_file][2])
            if x not in res[y][single_file][2]:
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
            susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1
    

print(str(susp))
    
        
    
    
