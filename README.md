# Tarantula in Python      

CSC 510- Software Engineering  
Project Report 1b

#Goals

 Our goal in this project is to create a tool that can help developers with unit testing. We want to make a tool like Tarantula (which is available for Ruby) in Python.
 
  * Implement a line coverage and fault localization tool in Python

  * Our implementation of Tarantula in Python for Fault Localization

  * Coverage.py and FigLeaf.py (our 2 techniques) are python code coverage libraries which we will integrate into our code coverage design.

#Background

  * As a software product expands and becomes more complex with the addition of features and functionality, the chances of bugs and defects being introduced in the software increases. This poses a problem to the development and QA team to know how many lines of code are being covered by their unit tests and where certain failures are occuring, so as to prevent bug escapes which bring down the quality of the product.
  * Developers need to know where certain unit tests fail in an efficient way and what pieces of the code are not being covered by the existing unit tests.  
  * Our system will help python developers do the following:  
      - Locate the most likely lines which caused any of the unit tests to fail using our python implementation of Tarantula.
      - And point out lines of code which were not covered during the unit test


#Methods

<b>What is Code Coverage?  </b>

The Wikipedia definition of code coverage  is "In computer science, code coverage is a measure used to describe the degree to which the source code of a program is tested by a particular test suite. A program with high code coverage has been more thoroughly tested and has a lower chance of containing software bugs than a program with low code coverage."  

Finding out the coverage that a test suite/test case gives is very beneficial for a developer; she can find out which functions have not been tested, what conditions have not been tested very easily.  

We are using coverage.py and figleaf.py, two Python libraries for code coverage and providing the coverage.  

<b>What is fault localization?</b>

Fault localization is a process to find the location of faults. It determines the root cause of the failure. It identifies the causes of abnormal behaviour of a faulty program. It identifies exactly where the bugs are. (This definition has been taken from the paper "Fault Localization for Java Programs Using Probabilistic Program Dependence Graph" [1] )  

Tarantula is a tool developed in Ruby which performs fault localization.  

<b>How to find who is the culprit?</b>

Tarantula calculates the "suspiciousness" of a line based on the formula : 

suspiciousness(e) = (failed(e)/total failed)/((passed(e)/total passed)+(failed(e)/total failed))

where 'e' denotes the line being checked.  

Our "two techniques":  

The two methods that we have implemented are :  
 - coverage.py
 - figleaf.py
 
These two are code coverage libraries in Python. We used each library and executed it on test cases. Using the result from these, we calculated the suspiciousness of each line. The color-coded suspiciousness value of each line can be seen from the html file "pyh.html". The line is red when the suspiciousness value is 1, that is, the probability of that line causing the test case to fail is 1. The line is green when the suspiciousness value is 0, that is, the probability of that line causing the test case to fail is 0. The line is grey when the suspiciousness value is -1, that is, that line has not been covered by any test case, or that line is not executable.   

#Our Approach and Testing Procedure

We pick up test files from the 'test' folder. Coverage/Figleaf is run on every test case in every file and their results collected. From the results of these, suspiciousness values are calculated for every source file in the 'src' folder. The lines of every source file (with line number) and the suspiciousness value of each line is displayed via HTML (pyh.html).  The results of coverage can be seen in the 'newhtmlcov' folder (index.html).  

This has been done for some sample test files that we created and also for one test file 'test_card.py' from a project 'pydealer' form github.  

For our system to run, we have made several assumptions and modified the test cases to cater to our assumptions. Our assumptions are:
 * All the source files are under the 'src' folder.  
 * All the test files are under the 'test' folder.   
 * Each test case returns a value 0 if successful and 1 if an assertion error is thrown.  
 * Every source file in the 'src' folder is part of the project as every source file in this folder is analyzed.  

Since the 'pydealer' project did not have these things, we had to modify the test file so that it would be compatible with our system.  

We imported the os and sys module and added the path of the src folder to the system path so it could look for the source files in the 'src' folder.  Because of Python versioning issues, instead of assertX methods we had to use assert keyword. Also, every test case returns a value of 0 it if passes and 1 if it fails. This is required to find how how many test cases have passed and failed for suspiciousness calculation.  

#Results

#Discussion

#Conclusion

#Future Work

One possible improvement can be to get rid of the assumptions, that is, the folder structure can be dynamic and can be taken as an input from the developer. To find out whether a test case has failed or not without having to return a 0 or 1 explicitly. The front end can be improved too; at the moment we have implemented a very basic UI.  

#References

[1] http://arxiv.org/ftp/arxiv/papers/1201/1201.3985.pdf  "Fault Localization for Java Programs Using Probabilistic Program
Dependence Graph" by A.Askarunisa, T. Manju and B. Giri Babu

[2] http://spideruci.org/papers/jones05.pdf "Empirical Evaluation of the Tarantula Automatic Fault-Localization Technique", by James A. Jones and Mary Jean Harrold
