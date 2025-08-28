#https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=problem-list-v2&envId=ajc81mgt

# Sliding window (fixed size, not dynamic)

def maxVowels(s: str, k: int) -> int:
    maxVowels = 0
    vowels = ['a','e','i','o','u']
    
    # The following commented-out approach is less efficient because it redundantly scans k elements for every step,
    # leading to O(n*k) time complexity instead of O(n).
    # left = 0
    # right = k
    
    # while right < len(s):
    #     curr = 0
    #     print(s[left:right])
    #     for j in range(left, right):
    #         if s[j] in vowels:
    #             curr += 1
    #     if curr > maxVowels:
    #         maxVowels = curr
    #     left += 1
    #     right += 1
    # return maxVowels

    curr = 0
    
    # initialize curr with first window value
    for i in range(k):
        if s[i] in vowels:
            curr += 1
    maxVowels = curr
    for i in range(k, len(s)):
        
        # Subtract the left character first to keep the window size consistent and accurately track vowel count
        #If you don’t subtract left first before adding the new one, your window grows beyond size k temporarily, and your count becomes inaccurate.
        if s[i-k] in vowels:
            curr -= 1
        #The if/elif version you had commented out assumes that the character coming in and the character going out are never both vowels—which isn’t safe. Using two if statements ensures both cases are handled independently, and correctly.
        if s[i] in vowels:
            curr += 1
            
        # The if/elif structure ensures mutually exclusive handling:
        # subtract first if needed, then check the new character to add
        # if s[i] in vowels and s[i-k] not in vowels: #add new element to the right 
        #     curr += 1 
        # elif s[i-k] in vowels: # remove element to left
        #     curr -= 1 
        maxVowels = max(maxVowels, curr)
        
    return maxVowels
s = "aeiou"
k = 2
print(maxVowels(s,k))