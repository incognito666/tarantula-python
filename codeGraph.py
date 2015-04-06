import string, os, sys

class CodeGraph(object):
	def __init__(self, 
				resultsArray = [],
				funcNameArray = [],
				funcResDict = {},
				outputFileName = None,
				path = None,
				sourcefiles = [],
				):
		super(CodeGraph, self).__init__()
		 
		self.resultsArray = resultsArray
		self.funcNameArray = funcNameArray
		self.outputFileName = outputFileName
		self.funcResDict = funcResDict
		self.path = path
		self.sourcefiles = sourcefiles


	def coverageOutputGather(self):
		file = open(self.outputFileName, 'r')
		for line in file:
			if '.py' in line[-4:]:
				self.funcNameArray.append(line[:-1])
			if 'result :' in line:
				self.resultsArray.append(line[-2:-1])
		print(self.funcNameArray)
		print(self.resultsArray)	 
		#return funcNameArray,resultsArray
		 
	def dot_to_png(self):
		files = os.listdir(self.path)  
		for f in files:
			if f[-3:]=="dot": 
				inputname = os.path.realpath(f)
				outputname = inputname.replace(".dot", ".png")
				os.system('c:\Program Files (x86)\Graphviz\bin\dot.exe -Tpng "' + os.path.realpath(f) + '" -o "' + outputname + '"')
			
	def dot_to_svg(self):  
		for f in os.listdir(self.path):
			if f[-3:]=="dot": 
				inputname = os.path.join(self.path, f)
				outputname = inputname.replace(".dot", ".svg")
				#print('C:\Graphviz\bin\dot.exe -Tsvg "' + inputname + '" -o "' + outputname + '"')
				os.system('C:\\Graphviz\\bin\\dot.exe -Tsvg "' + inputname + '" -o "' + outputname + '"')
				
			
		 
	def traceToDotConversion(self):
		for f in os.listdir(self.path): 
			#print(self.path)
			if f[-5:] == 'ftest':
				#outpath = os.path.realpath(f) + '\\codeGraph'
				outname = os.path.join(self.path,f.replace(".ftest", ".dot"))
				outputfile = open(outname , 'w')
				outputfile.write('digraph { \n')
				inputfile = open(os.path.join('codeGraph',f), 'r')
				flow = 0
				outline = ''
				resultIndex = -1
				for line in inputfile: 
					subline = line[:4]
					resultIndex = -1
					if '---' in subline:					
						funcIndex = line.find('funcname:')
						#print (funcIndex)
						funcName = line[funcIndex+10:-1]
						#resultIndex = self.funcNameArray.index(funcName)
						#print (funcName)
						modIndex = line.find('modulename:')
						#print (funcIndex)
						modName = line[modIndex+12:funcIndex-2]
						#print (modName)
						
						if flow == 0:
							resultIndex = self.funcNameArray.index(funcName)
							outline = '   ' + funcName
							flow = 1
						else:
							outline = outline + ' -> ' + funcName
							if self.resultsArray[resultIndex] == 0:
								outline = outline + ' [color=green];\n'
							elif self.resultsArray[resultIndex] == 1:
								outline = outline + ' [color=red];\n'
							else:
								outline = outline + ' [color=orange];\n'
							#for mod in range(0,len(self.sourcefiles)):
							#	if modName in self.sourcefiles[mod]:
							outputfile.write(outline)
							outline = '   ' + funcName
				outputfile.write('}')
				outputfile.close()
				
			
