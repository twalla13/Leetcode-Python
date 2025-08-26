# https://leetcode.com/problems/find-and-replace-pattern/

from typing import List


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    
    #Bijection and ONE to ONE so we need two data structures, one map and one set 
    #Every pattern[letter] maps to a words[letter] and no two letters map to the same letter
    #Going to use a map for pattern to word and then going to use a usedTracker to ensure no two words have already been mapped
    

    result = []
    for word in words:        
        patternToWord = {}
        usedWord = set()
        match = True # Flag to track if current word matches the pattern 
        
        if len(word) == len(pattern): #check if the word has the same length as the pattern
        # print("word and pattern have same length")
            for j in range(len(pattern)):
                c = pattern[j]
                if c not in patternToWord:
                    
                    #Check if the word letter has been used
                    if word[j] in usedWord:
                        match = False
                        break
                    
                    patternToWord[c] = word[j] #mapping the j position letter in pattern to the j position letter in word (forward mapping)
                    
                    usedWord.add(word[j]) #marking the word as used (reverse mapping)
                    
                #key already exists in map, make sure it maps to the correct word letter
                elif patternToWord[c] != word[j]:
                    match = False #Its not so update flag
                    break
            
            if match == True: #After each going through all the letters in pattern see if the word is a match 
                result.append(word)
                
                    
                    
    return result



words = ["bezhk","ohmgb","enbki","kcxmv","zimsl"]

result = findAndReplacePattern(words,"iusiq")

print(result) 