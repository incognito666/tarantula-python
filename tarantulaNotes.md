# Tarantula Notes
- Ruby Code Base: https://github.com/relevance/tarantula
- Docs on Fault Localization: http://spideruci.org/fault-localization/
	* Basically need to identify which code path of our test cases pass, fail or both. Can be through colors or a +/- system. We could do this line by line or by functions called. (Note: finding the algorithms used in the Ruby code would be a major plus but if it's too difficult to find/recreate in our time frame then this basic assumption would do.) 
	* The problem we have noticed for coverage and figleaf is that they just report the code coverage percentage and that it fails or passes but not where in the code the problem may lie. What we can do with our tarantula implementation is notify the developer of "possible" problematic areas of code to help them easily locate where their problem maybe.
	* Could handle expected failures vs. unexpected failures. 

- Python Trace: https://docs.python.org/2/library/trace.html
	* Could be good to use to get the lines that are being executed by our test (could even work with just functions). 
	* Could also see if we could modify the code in coverage and figleaf to obtain the path of the test cases instead of making it a completely separate process. 
	
- Metric of Suspicious code: Suspiciousness(i) = failed(i)/sqrt(totalFailed*(failed(i) + passed(i)))
	* i is the instruction or line of code
	* failed would be unexpected fails instead of expected failed tests. 

	


