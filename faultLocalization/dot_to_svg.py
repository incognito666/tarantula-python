import string, os, sys


files = os.listdir('.')  
for f in files:
    if f[-3:]=="dot": 
        inputname = os.path.realpath(f)
        outputname = inputname.replace(".dot", ".svg")
        os.system('c:\Program Files (x86)\Graphviz\bin\dot.exe -Tsvg "' + os.path.realpath(f) + '" -o "' + outputname + '"')