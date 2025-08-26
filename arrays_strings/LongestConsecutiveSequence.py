#https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=company&envId=bloomberg&favoriteSlug=bloomberg-more-than-six-months&difficulty=EASY

def longestConsecutive(nums: List[int]) -> int:
    #Must have time complexity O(n) so cannot sort O(nlogn)
    
    #Should use a set for constant time look ups
    #Convert the list into a set for O(1) look ups
    
    numsSet = set(nums)
    maxCount = 0
    for num in numsSet:
        if (num - 1) not in numsSet:
            # if one less then current num doesnt exist in the set 
            # then current num is the smallest potential num in that potential sequence
            
            # from here "walk forward" by
            current = num
            count = 1 # must start at one to count the current smallest num in the sequence
            while current + 1 in numsSet:
                current += 1
                count += 1
            if maxCount < count:
                maxCount = count
    
    return maxCount