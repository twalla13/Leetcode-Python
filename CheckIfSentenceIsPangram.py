#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/

from collections import defaultdict


def checkIfPangram(sentence: str) -> bool:
    
    #Pangram is a sentence where every letter of the English alphabet appears at least one
    #defaultdict(int) means “if you ask for a missing key, call int() (which gives 0) and return that.”
    #defaultdict lets us skip adding a map for all the letters
    #instead we only create entries when we see letters
    #ALSO THE CONSTAINT says that only lowercase alphabet letters are in sentence
        #soooo we only need to check if we have 26 entries
    
    freq = defaultdict(int)
    if len(sentence) < 26:
        return False
    for ch in sentence.lower():
        if ch.isalpha(): #using .lower and .isalpha to clean data so we can only check for 26 letters
            freq[ch] += 1
            
        
        
    return len(freq) == 26

result = checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(result)