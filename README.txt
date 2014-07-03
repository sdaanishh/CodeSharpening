Readme for Spelling Suggestor

INSTRUCTIONS FOR RUNNING:
1) Make sure you have Python 3.4.1 installed. It can be found here:
   Windows: https://www.python.org/downloads/windows/
   Linux/Unix: https://www.python.org/downloads/source/
   Mac OS X: https://www.python.org/downloads/mac-osx/
   
   You can identify which version you have by opening Command Prompt(Windows) and issuing the command py with no arguments, or in a Unix Terminal by issuing the command python with no arguments

2) Download and and extract the archive.  

3) Using command prompt(Windows), or a Unix terminal (Mac OS X, Linux), navigate to the folder where you have the extracted contents.

4) In Command Prompt(Windows) type in py controller.py or in a Unix Terminal type in python controller.py (You'll notice word pairs popping up on the command line, but it will take some time for the program to finish. At the end, in the directory where the other contents are will be suggestions.txt)

5) If you have the IDLE Python GUI, then you can open it, click open file, navigate to the directory where you extracted the contents, and select controller.py and run the code

ABOUT THE FILES:

	Controller.py: Program which initiates suggestion generation.  It issues the command to check each query against each word in the dictionary.  It also removes frequency counts from the set of possible suggestions.
	Comparator.py: Code which handles the comparing of two strings.  It needs a basic refactoring in that it needs a variable which holds the number of total modifications initially available.  Certain parts of the code need to refect that, but
	mergesort.py: Code that merge sorts a list of integers. 
	mergesortlists.py: Code that sorts a list of tuples of size of two, where the second element is an integer.  Used for sorting word frequency pairs.
	ComparingTests.py: Unit tests for Comparator.py.  You can run it the same way you ran controller.py
	mergesortTests.py: Unit test for mergesort.py. 
	mergesortlistTests.py: Unit test for mergesortlistTests.py
	__init__.py: Blank file, used to notify python that the directory is a module, which allows for imports from one python file to another
	word_frequency.csv: Given list of Words that are accepted, and their frequencies
	misspelled_queries.csv: list of all queries that are not correct in spelling
	assignment.md: Initial problem assignment file. Needs to be viewed in a browser
	README.txt: This file. Hopefully contains useful information.

ASSUMPTIONS:
	Here are a list of assumptions I made when working on the assignment. I should have asked wheter these were fair assumptions, but didn't.
	
	1) When checking a query against a word, it shouldn't worry about the case(TEETH is the same as teeth)
	
	2) No symbols in the alphabet.  A real word will not have any apostrophes or hyphens, thus, a query with these characters needs to have those characters counted against it
	
	3) A query is indeed a misspelled word, and will not appear in the word frequency list
	
ATTRIBUTIONS:
	The approach to this problem was completely my own (Something I am proud of). No help was used in that regard.
	Help in regards to some technical matters were found from
		
		1) Python Documentation: Provided useful help for string and list notation, loops, file reading and writing including csv files, appending, importing, and command line instructions
		   https://docs.python.org/3.4/contents.html
		
		2) Wikipedia - MergeSort: Had to brush up on merge sorting.(My bad...)
		   http://en.wikipedia.org/wiki/Merge_sort
	
	I was going to implement a dictionary lookup, or use some alignment techniques found in AN INTRODUCTION TO BIOINFORMATICS ALGORITHMS by Neil C. Jones and Pavel A. Pevzner but ran out of time.
	
