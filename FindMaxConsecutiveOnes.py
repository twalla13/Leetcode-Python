#https://leetcode.com/problems/max-consecutive-ones/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

def findMaxConsecutiveOnes(nums: List[int]) -> int:
    
    current = 0 
    longest = 0
    
    for num in nums:
        if num == 1 :
            current += 1
        else:
            if current > longest: 
                longest = current
            #Always want to reset the current even if I didnt have curr greater than longest
            current = 0
    
    if current > longest:
        return current
    
    return longest


