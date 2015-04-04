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
#def getName(filename):
#    fexec = open(filename,"r")
#    lines_executable.append(figleaf.get_lines(fexec))
#    fexec.close()
#    f=open(filename)
#    contents = f.read()
    #lines_executable.append(figleaf.get_lines(f))
    #print "Lines executable:"
    #print str(lines_executable)
#    start = contents.find('def')
#    end = contents.find('(',start)
#    f.close()
#    return contents[start+4:end]
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
	    	#print ("lines executabe for source file are:")
	    	#print str(lines_executable)
    return l

def getNames(filename):
    names = []
    fn = os.path.join('test',str(filename))
    #fn=filename
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

	

i=0

new_res={}
source_files = getSourceFiles()
print("Src files: ")
print(source_files)



##havent used this eiether anywhere
## code to get lines executable into a dictionary

dummy=0
dict_lines={}
for dummy in range(0,len(lines_executable)):
	s=lines_executable[dummy]
	dummy_list=[]
	while(len(s)!=0):
		a=s.pop()
		dummy_list.append(a)
	dict_lines[dummy]=dummy_list
	dummy+=1 
print ("\nLines executable in dictionary format:\n"+str(dict_lines))

total_failed = 0
score ={}
res={}
covered=[]
i=0
for file in os.listdir('test'):
	if fnmatch.fnmatch(file, 'test_*.py'):
		all_files={}
		print("\n")
		print('Test file:' + file)		
		str_file = str(file)
	        #print(str_file)
        	#path = os.path.join(os.getcwd(),'test')
        	#path = os.path.join(path,str_file)
		#path="/home/smruthi/figgy/test"
		#print ("path="+path)
		figleaf._t.c.clear()
		figleaf.start()
		fnew = file[:-3]
		#os.getcwd()
		#os.chdir(path)
		#print os.getcwd()
		#f_fullpath = os.path.join('test',f)
		#print("file is: "+f_fullpath)
		mod=importlib.import_module(fnew)
		#path = os.path.join(os.getcwd(),'test')
        	#path = os.path.join(path,str_file)
		#mod=imp.load_module('mm',file,path,)
		#mod=loader.load_module()
		print mod
		funcNames = getNames(file)
		print funcNames
	#	mod=importlib.import_module(f)
		for funcName in funcNames:
			if funcName != "":
				print('Test def:' + funcName)
				#mod=importlib.import_module(f)
				result = getattr(mod,funcName)()
				print result        
		score[i]=result
		print("result :"+str(result))
		print("------------------------------------------------------------------------------------------------------------------------------------------------")
		#	print("\n")
		figleaf.stop()
		for single_file in source_files:
			#path="/home/smruthi/figgy/src/"
			#os.chdir(path)
			print single_file
			fo=open('src/'+single_file,"r")
			all_functions=inspect.getmembers(figleaf._t,inspect.isfunction)
			all_files[single_file]=figleaf.get_data().gather_files()
		res[i]=all_files
		print (res[i])
		i+=1
print("score: "+str(score))
print("res: "+str(res))
print("---------------------------------------")

	##########################################################################################################
	## new_res gives executed lines from all the test files
		##########################################################################################################
			#s=res[i][single_file]
			#list_res=[]
			#while(len(s)!=0 ):
				#a=s.pop()
				#list_res.append(a)
			#new_res[i].append(a)
		#	print list_res
			#new_res[i]=list_res
	


for x in range(0,len(score)):
	total_failed += score[x]
total_tests = len(res)
total_passed = total_tests - total_failed
passed = 0
######################################################################
## converting the test3.py lines executable from set to list
######################################################################
bull=covered
susp=[]
while(len(bull)!=0):
	a=bull.pop()
	susp.append(a)

###########################################################################
## creating a final list structure similar to coverage.py res
## using list of lists for making this structure
###########################################################################
final_lists=[]
dummy_i=0;
while(dummy_i<len(new_res)):
	result_list=[]
	result_list.append('/home/smruthi/tarantula-python/figleaf_working/test3.py')
	#print str(result_list)
	result_list.append(susp)
	temp1=[]
	s= set(susp)-set(new_res[dummy_i])
	while(len(s)!=0):
		a=s.pop()
		temp1.append(a)
	result_list.append(temp1)
	result_list.append(temp1)
	dummy_i+=1
#	print dummy_i
	print str(result_list)
	final_lists.append(result_list)
###########################################################
## code to convert the final lists to a dictionary
###########################################################
dict_res={}
for temp_i in range (0,len(final_lists)):
	s=final_lists[temp_i]
	dict_res[temp_i]=s
print ("\nres: "+ str(dict_res))
#print("res1: "+str(dict_res[1][1]))
print("-------------------------------------------------------------------------------------------------------------------------------------------------")
print("Total tests: " + str(total_tests))
print("Total failed: "+str(total_failed))
print ("susp: "+str(susp))
print("res1: \n"+str(dict_res[1][1]))
i = 0
for x in dict_res[1][1]:
	failed_cases = 0
	passed=0
	for y in range(0,total_tests):
		print("y is "+str(y))
		print(dict_res[y][2])
		if x not in dict_res[y][2]:
			if score[y] == 1:
				failed_cases+=1
			else:
				passed+=1
			
	print("failed_cases: " + str(failed_cases) + " for line "+str(x))
	print("passed: " + str(passed) + " for line "+str(x))
	if (passed/total_passed)==0 and (failed_cases/total_failed)==0 :
		print("division by zero!!!!")
	else :
		susp[i] = (failed_cases / total_failed ) / ((passed/total_passed)+(failed_cases / total_failed ))
	i+=1
print ("\nsusp is: "+str(susp))
	
		
	
		
