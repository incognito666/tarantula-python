import os
import importlib
import subprocess
from modulefinder import ModuleFinder
import figleaf
from figleaf import internals
from importlib import import_module
import imp
import inspect
#############################################################################################################################################
##found out the lines executable from each file but havent used anywhere in the program. The lines executable considered are from test3.py##
##new_res has the lines executed from each test
##covered is a list with executable lines from test3.py
##final_lists is a list of lists with details of path of file, executable,executed
##dict_res is the dictionary with final_lists 
##############################################################################################################################################
lines_executable=[]
import fnmatch

def getSourceFiles():
    l = []
    for f in os.listdir('src'):
       # print(f)
        if os.path.isfile(os.path.join('src',f)) and f[0] is not '_':
	    if f[-2:]=='py':
            	l.append(f)
	    	fexec=open(os.path.join('src',f),"r")
	    	lines_executable.append(figleaf.get_lines(fexec))
	    	fexec.close()
    return l

def getNames(filename):
    names = []
    fn = os.path.join('test',str(filename))
    #print(fn)
    f = open(fn)
    contents = f.readlines()
    #print("func read start :")
    for line in contents:
        if not (line.strip().startswith("#")):
            start = line.find('def')
            if start != -1:
                end = line.find('(',start)
                #print(line)
                names.append(line[start+4:end])
    f.close()
    return names

i=0
new_res={}
source_files = getSourceFiles()
print("\nSource files are:")
print(source_files)
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
		print mod
		
		funcNames = getNames(file)
		
		for funcName in funcNames:
			if funcName != "":
				print('Test def:' + funcName)
				
				result = getattr(mod,funcName)()
				        
		score[i]=result
		
		print("------------------------------------------------------------------------------------------------------------------------------------------------")
		#	print("\n")
		figleaf.stop()
		for single_file in source_files:
			
			
			fo=open('src/'+single_file,"r")
			
			
		res[file]=figleaf.get_data().gather_files()
		
		i+=1
		temp_dict={}
		for single_file in source_files:
			if single_file in res[file].keys():
        			temp_dict[single_file]=res[file][single_file]

		new_res[file]=temp_dict



for x in range(0,len(score)):
	total_failed += score[x]
total_tests = len(res)
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
	for source in source_files:
		if source in new_res[test_f].keys():
			result_list=[]
			result_list.append(source)
			result_list.append(list(new_res[test_f][source]))
			s1=set(new_res[test_f][source])	
			s2=set(dict_lines[source])
			s=s2-s1
			result_list.append(list(s))
			result_list.append(list(s))
			dict_result_bck[source] =result_list
			
        dict_dict[i]=dict_result_bck
	final_lists[test_f]=dict_result_bck
	i+=1
print("score: "+str(score))
#print("result final is: "+str(final_lists))
print ("res:"+str(dict_dict))
print "\n"
print("*****************************************************************************************************************************************************************")
print("\n\t\t\t\t\tCalculating the suspiciousness\n")
print("*****************************************************************************************************************************************************************")
print("Total tests: " + str(total_tests))
print("Total failed: "+str(total_failed))
print ("\n")
susp={}

for single_file in source_files:
	if single_file in dict_dict[0].keys():
    		susp[single_file] = dict_dict[0][single_file][1]

print("Inital susp:"+ str(susp))
##susp = res[0][1]
all_executable_lines = susp


for single_file in source_files:
 if single_file in dict_dict[0].keys():
    print("For source file: "+ single_file)	
    print("All executable lines are: "+str(all_executable_lines[single_file]))
    #print "\n"
    i = 0
    for x in all_executable_lines[single_file]: ## to get executable lines for that file
        print("\nExec line :"+ str(x))

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
            print("failed_cases: " + str(failed_cases) + " for line "+str(x))
            print("passed: " + str(passed) + " for line "+str(x))
            ##passed = total_passed - failed_cases
            if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
##                print("division by zero!!!!")
                susp[single_file][i] = -1
            else :
                susp[single_file][i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
        i+=1

print ("\nThe suspicousness values are:")
print(str(susp))
print "\n\n"

	
		
	
		
