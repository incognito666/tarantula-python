import string, os, sys

class CodeGraph(object):
	 def __init__(self, 
				  resultsArray = [],
				  funcNameArray = [],
				  outputFileName = None,
				  path = None,
				  ):
		 super(CodeGraph, self).__init__()
		 
		 self.resultsArray = resultsArray
		 self.funcNameArray = funcNameArray
		 self.outputFileName = outputFileName
		 self.path = path


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
			
				
			
		 
	 def traceToDotCoversion(self):
		 files = os.listdir(self.path)
		 for f in files: 
			 if f[-5:] == 'ftest':
				outname = os.path.realpath(f).replace(".ftest", ".dot")
				outputfile = open(outname , 'w')
				outputfile.write('digraph {')
				inputfile = open(os.path.realpath(f), 'r')
				flow = 0
				outline = ''
				resultIndex = -1
				for line in inputfile: 
					subline = line[:4]
					resultIndex = -1
					if '---' in subline:
						modIndex = line.find('funcname:')
						print (modIndex)
						modName = line[modIndex+10:]
						resultIndex = self.funcNameArray.index(modName)
						print (modName)
						if flow == 0:
							outline = '   ' + modName
							flow = 1
						else:
							outline = outline + ' -> ' + modName
							if self.resultsArray[resultsIndex] == 0:
								 outline = outline + ' [color=green];\n'
							elif self.resultsArray[resultsIndex] == 1:
								 outline = outline + ' [color=red];\n'
							else:
								 outline = outline + ' [color=orange];\n'
							outputfile.write(outline)
							outline = '   ' + modName
				outputfile.write('}')
				outputfile.close()
				
			
