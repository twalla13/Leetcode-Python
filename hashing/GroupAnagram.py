#https://leetcode.com/problems/group-anagrams/description/

from ast import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    #Anagrams must be the same length since it uses all the original letters exactly once
    #Sort both anagrams and see if they are equal


    #check Notes 
   #Mapping charCount with list of strings
   
    result = defaultdict(list) #creates a default value of a list 

    for s in strs:
        count = [0] * 26 #a...z 
        #want to map a -> 0, b -> 1, and so on
        for c in s:
            #take the ascii value of the current value c and then subtract the ascii value of "a"
            count[ord(c) - ord("a")] += 1 
        #in python lists cannot be keys, need to change to tuple which is immutable 
        result[tuple(count)].append(s)
    
    return list(result.values())