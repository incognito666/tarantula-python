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
import tempfile
import csv
#############################################################################################################################################
##found out the lines executable from each file but havent used anywhere in the program. The lines executable considered are from test3.py##
##new_res has the lines executed from each test
##covered is a list with executable lines from test3.py
##final_lists is a list of lists with details of path of file, executable,executed
##dict_res is the dictionary with final_lists 
##############################################################################################################################################

def getColor(value):
    if value==0.0:
        return 'green'
    elif value==-1:
        return '#C6BABA'  ##Light Gray
    elif value==1.0:
        return 'red'
    else:
        return 'yellow'


                        #reader=csv.DictRea

def showSuspiciousness(files, susp):
	for single_file in files:
		i=0
		if (1==1):
			#print single_file
			#print "temp dict is"
			#print temp_dict
			
       			all_files[single_file]=temp_dict[i][single_file]
			#print all_files[single_file]
       			i=i+1
		
	#	print "final all files is\n"
	#	print all_files
	#	print "\n\n"
		#all_files=dict_dict
    		if not os.path.exists("susp"):
        		os.mkdir('susp')
    		indexPage = PyH('Index')
    		mytab = indexPage << table(border = '3')
    		tr0 = mytab <<tr()
  		tr0<<th('File Name')
   			#print files
    		for single_file in files:
			if (1==1):
	
        			last = single_file.rfind("/")
       				f1="susp/"+single_file[(last+1):-3]+".html"
        			tr1 = mytab << tr()
       				a1 = "<a href = '"+f1+"'> "+single_file+" </a>"
        			tr1 << td(a1)
    			indexPage.printOut('pyhfile.html')
    		for single_file in files:
			if (1==1):
				#print "in show1"
        			page=PyH(single_file)
        			mytab2=page <<table(border='3')
        			tr0=mytab2<<tr()
        			tr0<<th('Line Number')+th('Code')+th('Suspiciousness')
				#print "before open"
        			f=open(single_file,"r")
				#print "ader"
       				cnt = 1
        			line = f.readline()
        			while line:
					#print 'in while'
            				susp_value = -1
            				try:
						#print "in try/"
						#print susp[single_file][all_files[single_file][1].index(cnt)]
                				susp_value = susp[single_file][all_files[single_file][1].index(cnt)]
						#print susp_value
            				except:
						#print 'in except'
                				susp_value = -1
            				tr1=mytab2<<tr(bgcolor=getColor(susp_value))
           				tr1<<td(cnt)+td(line)+td(susp_value)
            				cnt+= 1
            				line = f.readline()
        			last = single_file.rfind("/")
        			page.printOut("susp/"+single_file[last+1:-3]+".html")




lines_executable=[]
import fnmatch

def getSourceFiles():
    l = []
    abs_p=[]  
    for f in os.listdir('src'):
       # print(f)
	fn=os.path.join('src',f)
	
        if os.path.isfile(fn) and f[0] is not '_':
	    if f[-2:]=='py':
            	l.append(f)
		abs_p.append(fn)
	    	fexec=open(fn,"r")
	    	lines_executable.append(figleaf.get_lines(fexec))
	    	fexec.close()
    #print abs_p
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
    f.close()
    return names

i=0
new_res={}
source_files,abs_source_files = getSourceFiles()
print("\nSource files are:")
## code to get lines executable into a dictionary

dummy=0
dict_lines={}
#for dummy in range(0,len(lines_executable)):
for files in source_files:
	s=lines_executable[dummy]
	dummy_list=[]
	while(len(s)!=0):
		a=s.pop()
		dummy_list.append(a)
	dict_lines[files]=dummy_list
	dummy+=1 
print ("\nLines executable in each source file:\n"+str(dict_lines))

total_failed = 0
score ={}
res={}
needed_data={}
covered=[]
i=0
test_file=[]
print("\nRunning the tests")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
for file in os.listdir('test'):
	if fnmatch.fnmatch(file, 'test_*.py'):
		all_files={}
		
		print('Test file:' + file)
		print("\n")		
		test_file.append(file)
		str_file = str(file)
		figleaf._t.c.clear()
		figleaf.start()
		fnew = file[:-3]
		mod=importlib.import_module(fnew)
		
		funcNames = getNames(file)
		
		for funcName in funcNames:
			if funcName != "":
				print('Test def:' + funcName)
				
				result = getattr(mod,funcName)()
				        
		score[i]=result
		
		print("------------------------------------------------------------------------------------------------------------------------------------------------")
		#	print("\n")
		figleaf.stop()
			
		res[file]=figleaf.get_data().gather_files()
		#print res[file]
		temp_dict={}
		for single_file in source_files:
			print single_file
			if single_file in res[file].keys():
			
        			temp_dict["src/"+single_file]=res[file][single_file]
				#print res[file][single_file]
			else:
				temp_dict["src/"+single_file]=[]
		#print "we need is coverage analysis of source files\n"
		#print temp_dict
		new_res[i]=temp_dict
		tmpdir=tempfile.mkdtemp('.figleaf')
		figleaf.annotate_html.report_as_html(new_res[i],tmpdir,[],{})
		i+=1
#print " the new resu valies"
print temp_dict
for x in range(0,len(score)):
	total_failed += score[x]
total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0

print ("The following are the test cases run:"+ str(test_file))

###########################################################################
## creating a final list structure similar to coverage.py res
## using list of lists for making this structure
###########################################################################
final_lists={}
dict_dict={}
dict_result_bck={}
i=0
for i in range (0,len(new_res)):

		#print("HAte u")
		#print("test_f name in for loop:"+test_f)
		dict_result_bck={}
		for source in source_files:
		
			if "src/"+source in new_res[i].keys():
				#print new_res[i].keys()
				#print("I am found")
				result_list=[]
				result_list.append("src/"+source)
				result_list.append(dict_lines[source])
				#result_list.append(list(new_res[i]["src/"+source]))
				s1=set(new_res[i]["src/"+source])	
				s2=set(dict_lines[source])
				s=s2-s1
				result_list.append(list(s))
				result_list.append(list(s))
				dict_result_bck["src/"+source] =result_list
			else:
				#dum_l=[-1,-1,-1,-1]
				print ("I am not found\n")
				result_list=[]
				result_list.append(source)
				result_list.append(dict_lines[source])
 				s1=set([])
                                s2=set(dict_lines[source])
                                s=s2-s1
                                result_list.append(list(s))
                                result_list.append(list(s))
                                dict_result_bck["src/"+source] =result_list
		#print dict_result_bck	
        	dict_dict[i]=dict_result_bck
		#print test_f
		final_lists[i]=dict_result_bck
	
#print("score: "+str(score))
#print("result final is:"+str(final_lists))
print ("res:"+str(dict_dict))
print "\n"
print("*****************************************************************************************************************************************************************")
print("\n\t\t\t\t\tCalculating the suspiciousness\n")
print("*****************************************************************************************************************************************************************")
print("Total tests: " + str(total_tests))
print("Total failed: "+str(total_failed))
print ("\n")
susp={}


temp_dict=dict_dict
#print dict_dict
#print temp_dict
for single_file in abs_source_files:
	#if single_file in dict_dict[0].keys():
    	susp[single_file] = dict_dict[0][single_file][1]

#print("Inital susp:"+ str(susp))
##susp = res[0][1]
all_executable_lines = susp

#print "all"
#print all_executable_lines
#print 'all'
for single_file in source_files:
 #if single_file in dict_dict[0].keys():
    print("For source file: "+ "src/"+single_file)	
    print("All executable lines are: "+str(all_executable_lines["src/"+single_file]))
    #print "\n"
    i = 0
    for x in all_executable_lines["src/"+single_file]: ## to get executable lines for that file
        print("\nExec line :"+ str(x))

        failed_cases = 0
        passed=0
        for y in range(0,total_tests):
              #print("y is "+str(y))
              #print(res[y][single_file][2])
            if x not in dict_dict[y]["src/"+single_file][2]:
                if score[y] == 1:
                    failed_cases+=1
                else:
                    passed+=1
            print("failed_cases: " + str(failed_cases) + " for line "+str(x))
            print("passed: " + str(passed) + " for line "+str(x))
            ##passed = total_passed - failed_cases
            if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
##                print("division by zero!!!!")
                susp["src/"+single_file][i] = -1
            else :
                susp["src/"+single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
      	i+=1
#print final_lists
#print "abs"
#print "123444444444444444"
#print abs_source_files
#print "111111111111111111111111111111111111111"
#print str(susp)
#print temp_dict
showSuspiciousness(abs_source_files,susp)
print ("\nThe suspicousness values are:")
print(str(susp))
print "\n\n"

	
		
	
		
