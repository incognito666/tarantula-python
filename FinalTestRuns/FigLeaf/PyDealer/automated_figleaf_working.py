from __future__ import division
import os
import importlib
import subprocess
from modulefinder import ModuleFinder
import figleaf,figleaf.annotate_html
from figleaf import internals
from importlib import import_module
import imp
import inspect
from pyh import *
import time
import argparse
import tempfile
from codeGraph import CodeGraph
#############################################################################################################################################
##found out the lines executable from each file but havent used anywhere in the program. The lines executable considered are from test3.py##
##new_res has the lines executed from each test
##covered is a list with executable lines from test3.py
##final_lists is a list of lists with details of path of file, executable,executed
##dict_res is the dictionary with final_lists 
##############################################################################################################################################
lines_executable=[]
import fnmatch

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
    global all_files
    print ("In the HTTP loop")
    #print dict_dict[0]
    for single_file in files:
        if single_file in dict_dict[0].keys():
            all_files[single_file] = dict_dict[0][single_file]
    print (all_files)
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
        print os.path.abspath(fn)
        if os.path.isfile(fn) and f[0] is not '_':
                if f[-2:]=='py':
                    l.append(f)                    
                    #abs_p.append(os.path.abspath(fn))
                    abs_p.append(os.path.abspath(fn))
                    fexec=open(fn,"r")
                    lines_executable.append(figleaf.get_lines(fexec))
                    fexec.close()
    print ("This is abs_p")
    print abs_p
    return (l,abs_p)

def getNames(filename):
    names = []
    #fn = os.path.join('test',str(filename))
    #print(fn)
    #f = open(fn)
    f = open(filename)
    contents = f.readlines()
    # print("func read start :")
    for line in contents:
        if not (line.strip().startswith("#")):
            start = line.find('def')
            if start != -1:
                end = line.find('(',start)
                #print(line)
                names.append(line[start+4:end])
    f.close()
    return names

    
    
codegraph = CodeGraph()  
codegraph.path = os.getcwd() + '\\codeGraph'
start_time = time.time() 
i=0
new_res={}
source_files,abs_source_files = getSourceFiles()
for placeS in range(0,len(source_files)):
    codegraph.sourcefiles.append(source_files[placeS])
print("\nSource files are:")
print(abs_source_files)
## code to get lines executable into a dictionary

dummy=0
dict_lines={}
#for dummy in range(0,len(lines_executable)):
for files in abs_source_files:
	s=lines_executable[dummy]
	dummy_list=[]
	while(len(s)!=0):
		a=s.pop()
		dummy_list.append(a)
	dict_lines[files]=dummy_list
	dummy+=1 
print ("\nLines executable in each source file:\n"+str(dict_lines))


all_files={}
total_failed = 0
score ={}
res={}
needed_data={}
covered=[]
i=0
test_file=[]
result_dict = {}
print("\nRunning the tests")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'test_*.py'):
        
		
        #print('Test file:' + file)
        #print("\n")		
        test_file.append(file)
        str_file = str(file)
        #figleaf._t.c.clear()
        figleaf.start()
        fnew = file[:-3]
        mod=importlib.import_module(fnew)
        #print ("mod is: ")
        #print mod
        funcNames = getNames(file)
        codegraph.sourcefiles.append(file)
        for funcName in funcNames:
            if funcName != "":
                #print('Test def:' + funcName)
                if not os.path.exists("codeGraph"):    
                    os.mkdir('codeGraph')
                result = getattr(mod,funcName)()
                outName = fnew + '_-' + funcName + '.ftest'
                cgn = os.path.join('codeGraph',outName)
                tmp_pyfile = open('tmp.py', 'w')
                tmp_pyfile.write("import trace \nfrom " + fnew + " import " + funcName + ' \n\n\ntracer = trace.Trace(count=False, trace=True) \ntracer.runfunc(' + funcName + ") \n\n")
                tmp_pyfile.close
                codegraph.funcNameArray.append(funcName)
                codegraph.resultsArray.append(result)
                os.system('C:\Python27\python.exe tmp.py > "' + os.path.abspath(cgn) +'"')
				        
        score[i]=result

        #print("------------------------------------------------------------------------------------------------------------------------------------------------")
        #	print("\n")
        figleaf.stop()
        #for single_file in source_files:            
            #fo=open('src/'+single_file,"r")
            
            
        res[file]=figleaf.get_data().gather_files()
        #print('This is the res:')
        #print res
        #print ('\n\n\n')
        
        
        temp_dict={}
        for single_file in abs_source_files:
            if single_file in res[file].keys():
                    temp_dict[single_file]=res[file][single_file]

        new_res[file]=temp_dict
        if not os.path.exists(".figleaf"):    
            os.mkdir('.figleaf')
        tmpdir= os.getcwd() + '\\.figleaf'
        figleaf.annotate_html.report_as_html(new_res[file],tmpdir,[],{})
        #print('This is the new_res:')
        #print new_res
        #print ('\n\n\n')
        i+=1

total_tests = 0
# The 1 in ind_score references the value of the key.
for x in range(0,len(score)):
    #for ind_score in score[x].items():
    total_failed += score[x]
    total_tests += 1
total_passed = total_tests - total_failed
passed = 0




###########################################################################
## creating a final list structure similar to coverage.py res
## using list of lists for making this structure
###########################################################################
final_lists={}
dict_dict={}
dict_result_bck={}
i=0
for test_f in test_file:
    dict_result_bck={}
    for source in abs_source_files:
        if source in new_res[test_f].keys():
            result_list=[]
            result_list.append(source)
            #print dict_lines[source]
            result_list.append(list(dict_lines[source]))
            s1=set(new_res[test_f][source])
            #print s1
            s2=set(dict_lines[source])
            s=s2-s1
            #print s
            result_list.append(list(s))
            result_list.append(list(s))
            #res[test_f][source] =result_list
            #print result_list
            dict_result_bck[source] =result_list			
    dict_dict[i]=dict_result_bck
    final_lists[test_f]=dict_result_bck
    i+=1
print("score: "+str(score))
#print("result final is: "+str(final_lists))
print ("res: "+str(dict_dict))
print "\n"
print("*****************************************************************************************************************************************************************")
print("\n\t\t\t\t\tCalculating the suspiciousness\n")
print("*****************************************************************************************************************************************************************")
print("Total tests: " + str(total_tests))
print("Total failed: "+str(total_failed))
print("Total passed: "+str(total_passed))
print ("\n")
susp={}

#print ("something smells fishy.")
#print dict_dict[0]



#######################################################################################################
##############################################################################################################
##############################################################################################################
#################################################################################################################
for single_file in abs_source_files:
	if single_file in dict_dict[0].keys():
    		susp[single_file] =list( dict_dict[0][single_file][1])

#print("Inital susp:"+ str(susp))
##susp = res[0][1]
all_executable_lines = susp


for single_file in abs_source_files:
 if single_file in dict_dict[0].keys():
    #print("For source file: "+ single_file)	
    #print("All executable lines are: "+str(all_executable_lines[single_file]))
    #print "\n"
    i = 0
    for x in all_executable_lines[single_file]: ## to get executable lines for that file
        #print("\nExec line :"+ str(x))

        failed_cases = 0
        passed=0
        for y in range(0,total_tests):
              #print("y is "+str(y))
              #print(res[y][single_file][2])
            if x not in dict_dict[y][single_file][2]:
                if score[y] == 1:
                    failed_cases+=1
                else:
                    passed+=1
            #print("failed_cases: " + str(failed_cases) + " for line "+str(x))
            #print("passed: " + str(passed) + " for line "+str(x))
            ##passed = total_passed - failed_cases
            if ((total_passed)==0 and (total_failed)==0):
                susp[single_file][i] = -1
            elif total_passed == 0: 
                susp[single_file][i] = (failed_cases / total_failed ) / ((0)+(failed_cases / total_failed ))
            elif total_failed == 0 or failed_cases == 0: 
                susp[single_file][i] = 0
            else :
                susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1

print ("\nThe suspicousness values are: ")
print(str(susp))
print "\n\n"

total_time = time.time() - start_time
codegraph.traceToDotConversion()
codegraph.dot_to_svg()
showSuspiciousness(abs_source_files, susp)

print("Execution time: " + str(total_time) + " sec")

	
		
	
		
