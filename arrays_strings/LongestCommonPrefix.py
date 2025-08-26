#https://leetcode.com/problems/longest-common-prefix/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY 

def longestCommonPrefix(strs: list[str]) -> str:
    
    #Start with first word and common index i
    #compare each index at i in the other words to the first word
    #return the characters once the characters dont match
    #HOWEVER Edge Case: (Flower, Flowz, Flow) going out of bounds so need to find smallest string
    
    
     # Edge case: if the list is empty, return an empty string.
    if not strs:
        return ""
    
    # min_length = 0
    
    # for s in strs:
    #     if len(s) < min_length:
    #         min_length = len(s)
    # Find the length of the shortest string.
    # Issue: The original code above set min_length to 0. This always causes the loop to skip.
    # Correction: Use the length of the first string or the min() function.
    
    min_length = min(len(s) for s in strs)
    i = 0
    while i < min_length:
        #compare common index i with all the words
        #strs[0][i] = the first word in the list and that first words's index at i
        for s in strs:
            if s[i] != strs[0][i]:
                #only returns if there was characters not matching
                return s[:i] #return s up until i, exclusive
        i += 1
        
      # If all characters in the shortest string are common, return that prefix.
    return strs[0][:min_length]

strs = ["flower","flow","flight"]
result = longestCommonPrefix(strs)

print(result)  