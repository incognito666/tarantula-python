import trace 
from test.test_card9 import test_ge_func 


tracer = trace.Trace(count=False, trace=True) 
tracer.runfunc(test_ge_func) 

