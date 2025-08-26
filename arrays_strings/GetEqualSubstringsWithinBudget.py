#https://leetcode.com/problems/get-equal-substrings-within-budget/description/

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    #Dynamic sliding window 
    #We know this because its looking for a valid substring
    
    ans = 0 #window size
    curr = 0
    l = r = 0 
    
    for r in range(len(s)):
        asciiDiff = abs(ord(t[r]) - ord(s[r]))
        
        #grow the window
        curr += asciiDiff
        
        #if window after growth violates condition, shrink it until it doesnt
        while curr > maxCost:
            curr -= abs(ord(t[l]) - ord(s[l]))
            l += 1
        
        #update window size
        ans = max(ans, r - l + 1)
    return ans
    
result = equalSubstring( s = "abcd", t = "acde", maxCost = 0)
print(result)