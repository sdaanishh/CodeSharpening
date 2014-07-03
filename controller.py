import csv
from Comparator import querySuggestor
from mergesortlists import mergeSorterLists

class SuggestionGenerator:
        def generateSuggestions(self):

                queryList = [] #set of all queries
                dictionaryList = [] #set of all accepted words, and their frequencies
                returnSet = []# mapping of each query to possible suggestions

                mergerSorter = mergeSorterLists() #sorts out words based on their frequencies
                comparer = querySuggestor()# compares two strings to see if they are a possible suggestion
                with open('misspelled_queries.csv', newline = '') as csvfile: #read in queries
                        queries = csv.reader(csvfile, delimiter=' ', quotechar='|')
                        for row in queries:
                                queryList.append(row)
                csvfile.closed
                with open('word_frequency.csv', newline = '') as csvfile2:#read in words and frequencies
                        words = csv.reader(csvfile2, delimiter = ' ',quotechar='|')
                        for row in words:
                                dictionaryList.append(row[0])
                csvfile2.closed
                for query in queryList:#for each query, check it agaainst all the dictionary words to see if it is a possible suggestion.
                        temp = []#list of dictionary pairs of words and their frequencies that are a match for a given query
                        for word in dictionaryList:
                                count = 0
                                for letter in word:
                                        if(letter == ','):
                                                tempword = word[0:count] #word portion of a dictionary entry
                                                if(comparer.possibleMatch(query[0],tempword,0,0)):#check if its a match
                                                        print(query[0],tempword)
                                                        temp.append([tempword,word[count+1:]])#add the word and the frequency as individual set 
                                        count = count+1
                        returnSet.append([query,temp])#append the query and the set of words and their frequencies
                for entry in returnSet:
                        t = mergerSorter.mergeSortList(entry[1])#sort out the word frequency portions
                        i = 0
                        for line in t:# remove the frequencies, as the words are sorted
                                t[i] = line[0]
                                i = i+1
                        entry[1] = t#update the returnSet with just the words
                with open('suggestions.txt','w') as f:
                        for mapping in returnSet:
                                f.write(mapping[0][0])
                                f.write(': [')
                                count = 0
                                for word in mapping[1]:#write in the word in single quotes for each word
                                        f.write("'")
                                        f.write(word)
                                        f.write("'")
                                        if(count < len(mapping[1])-1):#write in a comma after, unless it is the last word
                                                f.write(", ")
                                        count = count +1
                                f.write(']\n')

                f.closed
        
generate = SuggestionGenerator()
generate.generateSuggestions()
