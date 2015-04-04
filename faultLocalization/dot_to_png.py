import string, os, sys


files = os.listdir('.')  
for f in files:
    if f[-3:]=="dot": 
        inputname = os.path.realpath(f)
        outputname = inputname.replace(".dot", ".png")
        os.system('c:\Program Files (x86)\Graphviz\bin\dot.exe -Tpng "' + os.path.realpath(f) + '" -o "' + outputname + '"')