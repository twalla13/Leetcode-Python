# https://www.youtube.com/watch?v=XYQecbcd6_c&ab_channel=NeetCode

#https://leetcode.com/problems/longest-palindromic-substring/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

def longestPalindrome(s: str) -> str:

    #Palindrome f*cking suck 
    #Assume i is the center of the palindrome 
    #Then check the left and right pointers to see if the characters are equal
    #This works good for palindromes of odd lengths but ...
    #but even palindrome lengths is an edge case so we only check the current index and the index to the right (i, i+1)
    
    res = ""
    resLen = 0
    
    #Go through all indices and pretend like the current one is the center
    #For each position in string we try two types of centers:
        #character itself (ood length with single center character)
        #gap between the character and the next one (even length with no single center char)
    for i in range(len(s)):
        
        #odd length palindromes
        l, r = i, i # left and right pointers starting at i
        #Example: In "racecar", when i = 3 (the 'e'), we expand to check if "racecar" is a palindrome
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen: #current length of palindrome (r - l + 1) 
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1 #expand outward on both sides to see if letters match 
            r += 1 #expand outward on both sides to see if letters match 
            
            
        #even length palindromes have no single center character 
        l, r = i, i+1 # left starts a i and right starts at i+1, adjacent positons
        #Example: In "abba", when i = 1, we check if "bb" is a palindrome, then expand to "abba"
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen: #current length of palindrome (r - l + 1) 
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1
                
    return res


result = longestPalindrome("babad")

print(result) 