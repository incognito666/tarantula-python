import os
import importlib.machinery
import subprocess
from coverage import coverage
from pyh import *

def showSuspiciousness(files, susp):
##    files = ['test3.py','test4.py']
    print(files)
    for single_file in files:
        all_files[single_file] = cov.analysis(single_file)
    if not os.path.exists("susp"):    
        os.mkdir('susp')
    print("++++++++++++++++++++++++++++++")
    print(all_files)
    indexPage = PyH('Index')
    mytab = indexPage << table(border = '3')
    tr0 = mytab <<tr()
    tr0<<th('File Name')
    for single_file in files:
        last = single_file.rfind("\\")
        f1="susp\\"+single_file[(last+1):-3]+".html"
        print("<<<<<<<<<<<<<<")
        print(f1)
        tr1 = mytab << tr()
        a1 = "<a href = '"+f1+"'> "+single_file+" </a>"
        tr1 << td(a1)
    indexPage.printOut('pyhfile.html')
    for single_file in files:
        page=PyH(single_file)
        mytab2=page <<table(border='3')
        tr0=mytab2<<tr()
        tr0<<th('Line Number')+th('Code')+th('Suspiciousness')
##        f=open(os.path.join("../",single_file),"r")
        f=open(single_file,"r")
        cnt = 1
        line = f.readline()
        while line:
            susp_value = -1
##            print("exec ",all_executable_lines[single_file])
            
            try:
##                print(cnt," index is ",all_files[single_file][1].index(cnt))
                susp_value = susp[single_file][all_files[single_file][1].index(cnt)]
            except:
##                print(cnt," index is ")
                susp_value = -1
            tr1=mytab2<<tr()
            tr1<<td(cnt)+td(line)+td(susp_value)
            cnt+= 1
            line = f.readline()
            #path = os.path.join('susp',single_file[:-3])
        last = single_file.rfind("\\")
        print(">>>>>>>>>>>>>>>>>>>>>>>")
        print(single_file[last+1:-3]+".html")
        page.printOut("susp\\"+single_file[last+1:-3]+".html")
        
    
    
def getSourceFiles():
    l = []
    abs_p = []
    for f in os.listdir('src'):
        print(f)
        fn = os.path.join('src',f)
        if os.path.isfile(fn) and f[0] is not '_':
            l.append(f)
            abs_p.append(fn)
        elif f[0] is not '_':
            for f1 in os.listdir('src/'+f):
                fnew = os.path.join(os.path.join('src',f),f1)
                if os.path.isfile(fnew) and f1[0] is not '_':
                    l.append(f1)
                    abs_p.append(fnew)
    return (l,abs_p)

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
source_files,abs_source_files = getSourceFiles()
print("Src files")
print(source_files)
print("abs_src ",str(abs_source_files))
print("///////////////////////////////")
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
                #print(funcName)
                result = getattr(mod,funcName)()
        score[i]=result
        #print("result :"+str(result))
        cov.stop()
        cov.html_report(directory = file)
        print("**************************")
        for single_file in abs_source_files:
            all_files[single_file] = cov.analysis(single_file)
        res[i]=all_files
##        print(res[i])
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

for single_file in abs_source_files:
    susp[single_file] = res[0][single_file][1]

print("Susp", susp)
##susp = res[0][1]
all_executable_lines = susp
##print("susp: "+str(susp))
##print("res1"+str(res[1][1]))
## for each file in source_files calc suspiciousness

for single_file in abs_source_files:
    print("for ",single_file)
    print(all_executable_lines[single_file])
    i = 0
    for x in all_executable_lines[single_file]: ## to get executable lines for that file
##        print("Exec line ",x)
        failed_cases = 0
        passed=0
        for y in range(0,total_tests):
##            print("y is "+str(y))
##            print(res[y][single_file][2])
            if x not in res[y][single_file][2]:
                if score[y] == 1:
                    failed_cases+=1
                else:
                    passed+=1 
            #print("failed_cases: " + str(failed_cases) + " for line "+str(x))
            #print("passed: " + str(passed) + " for line "+str(x))
            ##passed = total_passed - failed_cases
            if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
##                print("division by zero!!!!")
                susp[single_file][i] = -1
            else :
                susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1

##print("all exex is ",str(res[0]))  
showSuspiciousness(abs_source_files, susp)
print(str(susp))
    
        
    
    
