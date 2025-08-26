#https://leetcode.com/problems/decode-the-message/description/

#Hashmap example

from collections import defaultdict


def decodeMessage(key: str, message: str) -> str:
    
    #You only care about the first occurrence of each of the 26 distinct letters. 
    
    #loop through key and message, to create map
    #ignore spaces 
    mapping = {} #key - > alphabet
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    aIndex = 0
    res = []
    
    for ch in key:
        if ch == " ":
            continue #skip spaces
        if ch in mapping: 
            continue #skip repeats since we dont finish the for block
        mapping[ch] = alphabet[aIndex]  
        aIndex += 1
        
        if aIndex == len(alphabet): #reached length of alphabet
            break
    
    
    for m in message:
        if m == " ":
            res.append(" ")
        else:
            res.append(mapping[m])
        
    return "".join(res)
    
key1 = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

result = decodeMessage(key1, message)

print(result) 