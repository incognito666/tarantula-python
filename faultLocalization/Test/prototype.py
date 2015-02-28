import trace
import string, os, sys
from Testrecurse import recurse

funcName = 'recurse'
args = 2
file = open('output.ftest', 'w')
sys.stdout = file
tracer = trace.Trace(count=False, trace=True)
tracer.runfunc(recurse, 2)
sys.stdout = sys.__stdout__

# files = os.listdir('.\output')
# outputfile = open(os.path.join('output', 'recurse.ftest') , 'w')
# for f in files: 
#     if f[-5:] == 'cover':
# 		outputfile.write(os.path.realpath(f) + '\n\n')
# 		inputfile = open(os.path.join('output', f), 'r')
# 		for line in inputfile: 
# 			subline = line[:6]
# 			if ':' in subline:
# 				newline = '+ ' + line
# 			elif '>>>>>>' in subline:
# 				newline = '- ' + line
# 			else:
# 				newline = line
# 			outputfile.write(newline)
        
		
