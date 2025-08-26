#https://leetcode.com/problems/word-pattern/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY



def wordPattern(pattern: str, s: str) -> bool:
    #Hashmap patternLetter : sWord 
        #loop through the pattern 
            #if the (letter, word) doesnt exist hashmap, add it
            #if does exist in hashmap continue
            #if the letter exists in the map without the correct value or if the word exists in the map without the correct key, return false 
            
     # maps each pattern letter to its assigned word (as a single string)
    mapping = {}              
    # tracks words already assigned to avoid two letters sharing the same word
    used = set()             
    strs = s.split()

    if len(pattern) != len(strs): #check if list and pattern have same length
        return False


    for i in range(len(pattern)):
        c = pattern[i]
        w = strs[i]
        print("i, pattern[i],strs[i]", i, pattern[i], strs[i])
        
        #check if the key is in the map
        if c not in mapping:
            
            #check if the word the will be associated with the new key is in already in map
            if w in used:
                return False
            
            #if value doesnt exist in the map already, associate with new key
            mapping[c] = w
            used.add(w)
            print("if")
            
        #key already exists in map
        else:
            if mapping[c] != w:
                return False 
        print(map)

    return True

result = wordPattern("aaaa","aa aa aa aa")

print(result) 