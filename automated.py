import os
import importlib.machinery
import subprocess
from coverage import coverage
from pyh import *


def showSuspiciousness(files, susp):
    for single_file in files:
        all_files[single_file] = cov.analysis(single_file)
    if not os.path.exists("susp"):    
        os.mkdir('susp')
    indexPage = PyH('Index')
    mytab = indexPage << table(border = '3')
    tr0 = mytab <<tr()
    tr0<<th('File Name')
    for single_file in files:
        last = single_file.rfind("\\")
        f1="susp\\"+single_file[(last+1):-3]+".html"
        tr1 = mytab << tr()
        a1 = "<a href = '"+f1+"'> "+single_file+" </a>"
        tr1 << td(a1)
    indexPage.printOut('pyhfile.html')
    for single_file in files:
        page=PyH(single_file)
        mytab2=page <<table(border='3')
        tr0=mytab2<<tr()
        tr0<<th('Line Number')+th('Code')+th('Suspiciousness')
        f=open(single_file,"r")
        cnt = 1
        line = f.readline()
        while line:
            susp_value = -1
            try:
                susp_value = susp[single_file][all_files[single_file][1].index(cnt)]
            except:
                susp_value = -1
            tr1=mytab2<<tr()
            tr1<<td(cnt)+td(line)+td(susp_value)
            cnt+= 1
            line = f.readline()
        last = single_file.rfind("\\")
        page.printOut("susp\\"+single_file[last+1:-3]+".html")
        
def getSourceFiles():
    l = []
    abs_p = []
    for f in os.listdir('src'):
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
    f = open(fn)
    contents = f.readlines()
    for line in contents:
        if not (line.strip().startswith("#")):
            start = line.find('def')
            if start != -1:
                end = line.find('(',start)
                names.append(line[start+4:end])
    f.close()
    return names

   
cov = coverage()    
import fnmatch
i=0
res = {} #to store the cov.analysis for each file in each test
source_files,abs_source_files = getSourceFiles()
total_failed = 0
score ={}
for file in os.listdir('test'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        all_files = {}
        str_file = str(file)
        path = os.path.join(os.getcwd(),'test')
        path = os.path.join(path,str_file)
        cov.erase()
        cov.start()
        f = file[:-3]
        loader = importlib.machinery.SourceFileLoader('mmm', path)
        mod = loader.load_module()
        funcNames = getNames(file)
        for funcName in funcNames:
            if funcName  != "":
                result = getattr(mod,funcName)()
        score[i]=result
        cov.stop()
        cov.html_report(directory = file)
        for single_file in abs_source_files:
            all_files[single_file] = cov.analysis(single_file)
        res[i]=all_files
        i+=1
for x in range(0,len(score)):
    total_failed += score[x]
total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0

## to handle multiple src files, susp will now be a dict
## with key as filename in /src folder and value as it's susp value
susp = {}

for single_file in abs_source_files:
    susp[single_file] = res[0][single_file][1]

all_executable_lines = susp
## for each file in source_files calc suspiciousness
for single_file in abs_source_files:
    i = 0
    for x in all_executable_lines[single_file]: ## to get executable lines for that file
        failed_cases = 0
        passed=0
        for y in range(0,total_tests):
            if x not in res[y][single_file][2]:
                if score[y] == 1:
                    failed_cases+=1
                else:
                    passed+=1 
            if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
                susp[single_file][i] = -1
            else :
                susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1

showSuspiciousness(abs_source_files, susp)
print("suspiciousness is : ",str(susp))
    
        
    
    
