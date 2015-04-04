# CSC 510- Software Engineering
Tarantula in Python
Project Report 1b

#Goals

  * Implement a line coverage and fault localization tool in Python

  * Our implementation of Tarantula in Python for Fault Localization

  * Coverage.py and FigLeaf.py (our 2 techniques) are python code coverage libraries which we will integrate into our code coverage design.



#Background

  * As a software product expands and becomes more complex with the addition of features and functionality, the chances of bugs and defects being introduced in the software increases. This poses a problem to the development and QA team of how much code is being covered by their unit tests and where are certain failures occuring, to prevent bug escapes which bring down the quality of the product.
  * Developers need to know where certain unit tests fail in an efficient way and what pieces of the code are not being covered by the existing unit tests.  
  * Our system will help python developers do the following:  
      - Locate the most likely lines which caused any of the unit tests to fail using our python implementation of Tarantula.
      - And point out lines of code which were not covered during the unit test


#Methods

What is Code Coverage?  

The Wikipedia definition of code coverage  is "In computer science, code coverage is a measure used to describe the degree to which the source code of a program is tested by a particular test suite. A program with high code coverage has been more thoroughly tested and has a lower chance of containing software bugs than a program with low code coverage."  



What is fault localization?

How to calculate fault localization?

Our Approach:  

The two methods that we have implemente are :  
 - coverage.py
 - figleaf.py
 
These two are code covergae libraries in Python.  
We used each library and executed it on test cases.  
Using the result from these, we calculated the suspiciousness of each line.  
The color-coded suspiciousness value of each line can be seen from the html file "pyh.html".  
The line is red when the suspiciousness value is 1, that is, the probability of that line causing the test case to fail is 1.   
The line is green when the suspiciousness value is 0, that is, the probability of that line causing the test case to fail is 0. 
The line is grey when the suspiciousness value is -1, that is, that line has not been covered by any test case, or that line is not executable.   


#Test Procedure


#Results

#Discussion

#Conclusion

#Future Work

#References


