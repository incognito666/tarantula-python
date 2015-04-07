import os, sys
import importlib.machinery
import subprocess
from coverage import coverage
from pyh import *
import time
from codeGraph import CodeGraph
import trace

def getColor(value):
    if value==0.0:
        return 'green'
    elif value==-1:
        return '#C6BABA'  ##Light Gray
    elif value==1.0:
        return 'red'
    else:
        return 'yellow'

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
            tr1=mytab2<<tr(bgcolor=getColor(susp_value))
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
codegraph = CodeGraph()  
codegraph.path = os.getcwd() + '\\codeGraph'
import fnmatch
start_time = time.time() 
i=0
res = {} #to store the cov.analysis for each file in each test
source_files,abs_source_files = getSourceFiles()
for placeS in range(0,len(source_files)):
    codegraph.sourcefiles.append(source_files[placeS])
total_failed = 0
total_tests = 0
score ={}
countup = 0
for file in os.listdir('test'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        all_files = {}
        str_file = str(file)
        path = os.path.join(os.getcwd(),'test')
        path = os.path.join(path,str_file)
        cov.erase()
        ####cov.start()
        f = file[:-3]
        loader = importlib.machinery.SourceFileLoader('mmm', path)
        mod = loader.load_module()
        #print (mod)
        funcNames = getNames(file)
        codegraph.sourcefiles.append(file)
        result = 0
        print("result is --------------- ",result)
        for funcName in funcNames:
            result = 0###
            if funcName  != "":
                cov.erase() ###
                cov.start() ###
                result = getattr(mod,funcName)()
                total_tests+= 1
##                if not os.path.exists("codeGraph"):    
##                    os.mkdir('codeGraph')	
                #codegraph.path = '.\codeGraph'
##                outName = f + '_-' + funcName + '.ftest'
##                cgn = os.path.join('codeGraph',outName)
##                tmp_pyfile = open('tmp.py', 'w')
##                tmp_pyfile.write("import trace \nfrom test." + f + " import " + funcName + ' \n\n\ntracer = trace.Trace(count=False, trace=True) \ntracer.runfunc(' + funcName + ") \n\n")
##                tmp_pyfile.close
##                codegraph.funcNameArray.append(funcName)
##                codegraph.resultsArray.append(result)
                #cg_file = open(cgn, 'w')
                #sys.sdtout = cg_file
                #tracer = trace.Trace(count=False, trace=True)
                #tracer.runfunc(mod.funcName())
##                os.system('C:\Python34\python.exe tmp.py > "' + os.path.abspath(cgn) +'"')
##                os.remove("tmp.py")
                #sys.stdout = sys.__stdout__
                score[i]=result
                print("result is --------------- ",result)
                cov.stop()
                cov.html_report(directory = file)
                for single_file in abs_source_files:
                    all_files[single_file] = cov.analysis(single_file)
                res[i]=all_files
                i+=1
####        score[i]=result
####        print("result is --------------- ",result)
####        cov.stop()
####        cov.html_report(directory = file)
####        for single_file in abs_source_files:
####            all_files[single_file] = cov.analysis(single_file)
####        res[i]=all_files
####        i+=1
print(res)
print("\n\n\n\n")
print(score)
for x in range(0,len(score)):
    total_failed += score[x]
##total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0

print("\n\t\t\t\t\tCalculating the suspiciousness\n")
print("*****************************************************************************************************************************************************************")
print("Total tests: " + str(total_tests))
print("Total failed: "+str(total_failed))
print("Total passed: "+str(total_passed))
print ("\n")

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
##                print("Are we here when y = " + str(y))
                if score[y] == 1:
                    print("We hit failed test Case.")
                    failed_cases+=1
                else:
                    passed+=1 
            if ((total_passed)==0 and (total_failed)==0):
                susp[single_file][i] = -1
            elif total_passed == 0: 
                susp[single_file][i] = (failed_cases / total_failed ) / ((0)+(failed_cases / total_failed ))
            elif total_failed == 0 or failed_cases == 0: 
                susp[single_file][i] = 0
            else :                
                susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1

showSuspiciousness(abs_source_files, susp)
print("suspiciousness is : ",str(susp))
    
total_time = time.time() - start_time
##codegraph.traceToDotConversion()
##codegraph.dot_to_svg()

print("Execution time: " + str(total_time) + " sec")
        
    
    
