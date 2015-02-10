from coverage import coverage
cov = coverage()
cov.erase()
cov.start()
import test1
##import test3

##test1.runTests()
score_a = test1.runA()

cov.stop()
results = cov.analysis('test3.py')
cov.annotate('test3.py')
cov.html_report(directory='testA')
cov.erase()

cov.start()
score_b = test1.runB()
cov.stop()
results1 = cov.analysis('test3.py')
cov.annotate()
print(results)
print(results1)
cov.html_report(directory='testB')

##calculate suspiciousness
total_failed = score_a + score_b
print(total_failed)

susp = results[1]
i = 0
for x in results[1]:
    failed_cases = 0
    # for runA
    if x in results[2]:
        failed_cases += 1

    if x in results1[2]:
        failed_cases += 1
    total_passed = len(susp) - failed_cases
    susp[i] = (failed_cases / total_failed ) / ((total_passed/ 
        
    
    
