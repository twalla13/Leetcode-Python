#https://leetcode.com/problems/ransom-note/ 

from collections import defaultdict


def canConstruct(ransomNote, magazine):
    """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
    """   
    #Create a map with the magazine characters and their occurrences
    #the map function in python map(function, iterable) is used...
    #Parameter:
    # function: The function we want to apply to every element of the iterable.
    # iterable: The iterable whose elements we want to process.
    
    #what you are actually doing is similar to JS where you have an object with key/value pairs
    #python does have library for "dictionaries" (java equivalent of hashmaps) for counting occurrences of elements
    #defualtdict: basically makes a dictionary object you can populate, It is a sub-class of the dictionary class that returns a dictionary-like object
    #The difference from dictionary is, It provides a default value for the key that does not exist and never raises a KeyError.
    
    #but even better they have Counter class that can work with any collection in Python3
    counter = defaultdict(int)
    for c in magazine:
        counter[c] += 1
    
    #iterate through the ransomeNote
    #if the current letter in the ransomeNote doesnt exist in the dict then return false
    #if the current letter in the note exists in the map AND its dictionary value is 1 
        #delete the letter from the dict
    #else the current letter in the note exists in the map and its dict value > 1
        #decrement dict value
        
    for c in ransomNote:
        if c not in counter:
            return False
        elif counter[c] == 1: #counter is dict so we can look up the key (c) by array notation
            del counter[c]
        else:
            counter[c] -= 1
    
    return True
    
    

    
    
        
# Call the function and print the result
result = canConstruct("aab","aba")
print(result) 