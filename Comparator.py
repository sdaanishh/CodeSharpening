#this compares two strings and comapres them, based on the alphabet of use
class querySuggestor:
    #this is the alphabet. Doesn't include apostrophies or hyphens
    alphabet = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J,''j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
#this method does the actual comparison.  It compares two strings, and returns true if they are a possible suggestion, and returns false otherwise.  It is a basic recursive descent,
#with various initial checks to prune un-needed recursive calls.  It descends for each position along the queryString, it isn't case specific, and doesn't consider apostrophies or hyphens.
#mod count keeps track of the modifications on string a, index count keeps track of how far along string a we are on
# Also need to refactor out a private number which keeps the number of maximum allowed modifications. ie Three modifications instead of two.
    def possibleMatch(self,a, b,modcount,indexcount):
        if(modcount > 2):return False#you've already modified the initial word more than two times, so the word isn't a match
        if(len(str(a)) < 1): return False# an empty string isn't really a query
        if(indexcount > len(str(a))):return False#if you've checked against all the positions, then no possiblities exist that result in a matc
        if(len(a) - len(b) > 2 - modcount or len(b)- len(a) > 2 - modcount):return False  ##Two insertions or two deletions represent the biggest change in the length of a string
        #consequently, if the length difference is more than two, it is going to be impossible to generate a match
        if(a == b):return True#if its the same string, than its a possible match
        if(modcount == 2 and a!=b):return False# if already modified string a two times, and the strings still don't match, not much else you can do
    
        aLetters = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
        #holds the frequencies of letters in string a
        bLetters = [['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]]
        #holds the frequencies of letters in string b, 
        for letter in a:#generate string a character frequencies, not case specific and no punctuation
            if(letter == 'a' or letter == 'A'):
                aLetters[0][1] = aLetters[0][1] +1
            if(letter == 'b' or letter == 'B'):
                aLetters[1][1] = aLetters[1][1] +1
            if(letter == 'c' or letter == 'C'):
                aLetters[2][1] = aLetters[2][1] +1
            if(letter == 'd' or letter == 'D'):
                aLetters[3][1] = aLetters[3][1] +1
            if(letter == 'e' or letter == 'E'):
                aLetters[4][1] = aLetters[4][1] +1
            if(letter == 'f' or letter == 'F'):
                aLetters[5][1] = aLetters[5][1] +1
            if(letter == 'g' or letter == 'G'):
                aLetters[6][1] = aLetters[6][1] +1
            if(letter == 'h' or letter == 'H'):
                aLetters[7][1] = aLetters[7][1] +1
            if(letter == 'i' or letter == 'I'):
                aLetters[8][1] = aLetters[8][1] +1
            if(letter == 'j' or letter == 'J'):
                aLetters[9][1] = aLetters[9][1] +1
            if(letter == 'k' or letter == 'K'):
                aLetters[10][1] = aLetters[10][1] +1
            if(letter == 'l' or letter == 'L'):
                aLetters[11][1] = aLetters[11][1] +1
            if(letter == 'm' or letter == 'M'):
                aLetters[12][1] = aLetters[12][1] +1
            if(letter == 'n' or letter == 'N'):
                aLetters[13][1] = aLetters[13][1] +1
            if(letter == 'o' or letter == 'O'):
                aLetters[14][1] = aLetters[14][1] +1
            if(letter == 'p' or letter == 'P'):
                aLetters[15][1] = aLetters[15][1] +1
            if(letter == 'q' or letter == 'Q'):
                aLetters[16][1] = aLetters[16][1] +1
            if(letter == 'r' or letter == 'R'):
                aLetters[17][1] = aLetters[17][1] +1
            if(letter == 's' or letter == 'S'):
                aLetters[18][1] = aLetters[18][1] +1
            if(letter == 't' or letter == 'T'):
                aLetters[19][1] = aLetters[19][1] +1
            if(letter == 'u' or letter == 'U'):
                aLetters[20][1] = aLetters[20][1] +1
            if(letter == 'v' or letter == 'V'):
                aLetters[21][1] = aLetters[21][1] +1
            if(letter == 'w' or letter == 'W'):
                aLetters[22][1] = aLetters[22][1] +1
            if(letter == 'x' or letter == 'x'):
                aLetters[23][1] = aLetters[23][1] +1
            if(letter == 'y' or letter == 'Y'):
                aLetters[24][1] = aLetters[24][1] +1
            if(letter == 'z' or letter == 'Z'):
                aLetters[25][1] = aLetters[25][1] +1
        for letter in b:# generate string b frequencies, not case specific and no frequency
            if(letter == 'a' or letter == 'A'):
                bLetters[0][1] = bLetters[0][1] +1
            if(letter == 'b' or letter == 'B'):
                bLetters[1][1] = bLetters[1][1] +1
            if(letter == 'c' or letter == 'C'):
                bLetters[2][1] = bLetters[2][1] +1
            if(letter == 'd' or letter == 'D'):
                bLetters[3][1] = bLetters[3][1] +1
            if(letter == 'e' or letter == 'E'):
                bLetters[4][1] = bLetters[4][1] +1
            if(letter == 'f' or letter == 'F'):
                bLetters[5][1] = bLetters[5][1] +1
            if(letter == 'g' or letter == 'G'):
                bLetters[6][1] = bLetters[6][1] +1
            if(letter == 'h' or letter == 'H'):
                bLetters[7][1] = bLetters[7][1] +1
            if(letter == 'i' or letter == 'I'):
                bLetters[8][1] = bLetters[8][1] +1
            if(letter == 'j' or letter == 'J'):
                bLetters[9][1] = bLetters[9][1] +1
            if(letter == 'k' or letter == 'K'):
                bLetters[10][1] = bLetters[10][1] +1
            if(letter == 'l' or letter == 'L'):
                bLetters[11][1] = bLetters[11][1] +1
            if(letter == 'm' or letter == 'M'):
                bLetters[12][1] = bLetters[12][1] +1
            if(letter == 'n' or letter == 'N'):
                bLetters[13][1] = bLetters[13][1] +1
            if(letter == 'o' or letter == 'O'):
                bLetters[14][1] = bLetters[14][1] +1
            if(letter == 'p' or letter == 'P'):
                bLetters[15][1] = bLetters[15][1] +1
            if(letter == 'q' or letter == 'Q'):
                bLetters[16][1] = bLetters[16][1] +1
            if(letter == 'r' or letter == 'R'):
                bLetters[17][1] = bLetters[17][1] +1
            if(letter == 's' or letter == 'S'):
                bLetters[18][1] = bLetters[18][1] +1
            if(letter == 't' or letter == 'T'):
                bLetters[19][1] = bLetters[19][1] +1
            if(letter == 'u' or letter == 'U'):
                bLetters[20][1] = bLetters[20][1] +1
            if(letter == 'v' or letter == 'V'):
                bLetters[21][1] = bLetters[21][1] +1
            if(letter == 'w' or letter == 'W'):
                bLetters[22][1] = bLetters[22][1] +1
            if(letter == 'x' or letter == 'x'):
                bLetters[23][1] = bLetters[23][1] +1
            if(letter == 'y' or letter == 'Y'):
                bLetters[24][1] = bLetters[24][1] +1
            if(letter == 'z' or letter == 'Z'):
                bLetters[25][1] = bLetters[25][1] +1

        index = 0
        aDifferenceCount =0# Sum of the number of occurences where a has more than b
        bDifferenceCount = 0#Sum of the number of occurences where b has more than a
        for letter in aLetters:
            if(letter[1] != bLetters[index][1]):
                if(letter[1] > bLetters[index][1]):
                    aDifferenceCount = aDifferenceCount + letter[1] - bLetters[index][1]#a has more of a character than b
                else:
                    bDifferenceCount = bDifferenceCount + bLetters[index][1] - letter[1]#b has more of a character than a
            index = index+1         
        if(aDifferenceCount + bDifferenceCount > int(4 - int(2*modcount) )): return False#the total differences between a and b can decrease by two for a single operation, namely the change.
        #Consequently, if the total number of differences is greater than the number of operations left times two,(because character changes decrease differences by two),
        #than it will be impossible to make a match
        
        for letter in bLetters:#try inserting every single letter
            if(letter[1] > 0):
                if not(letter[0] in b[0:indexcount]):
                    if(self.possibleMatch(str(str(a)[0:indexcount]+letter[0]+str(a)[indexcount:]),str(b),int(modcount+1),indexcount)):return True
        if(len(str(a)) > 1 ):#try deleting the current letter
            if(self.possibleMatch(str(a)[0:indexcount]+str(a)[indexcount+1:],str(b),int(modcount+1),indexcount)):return True
        for letter in bLetters:#try changing the current letter
            if(letter[1] > 0):
                if(self.possibleMatch(str(a)[0:indexcount]+letter[0]+str(a)[indexcount+1:],str(b),int(modcount+1),indexcount)):return True
        if(modcount < 2):#move on to the next letter, but only if modifications are still available, if not, then the method should have already returned true
            if(self.possibleMatch(str(a),str(b),int(modcount),indexcount+1)):return True
        return False#you've tried everything, but no luck


