#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY 



#https://youtu.be/pY2dYa1m2VM

def lengthOfLongestSubstring(s: str) -> int:
    #Sliding Window with Hashmap 
    seen = {} # letter, index
    length = 0
    left=0 # pointers for sliding window
    
    # add first character to hashmap
    for right in range(len(s)):
        character = s[right] # char at right pointer
        #if the character is in the map "seen" and the index of that character in the string is less than the left pointer then it is a repeated character
            #move the left pointer up 
        if character in seen and seen[character] >= left:
            left = seen[character] + 1
        else:
            #must add one for the right and left pointers
            length = max(length, right - left + 1)
        seen[character] = right
        
        
       
        
    return length



result = lengthOfLongestSubstring("abcabcbb")
print(result)