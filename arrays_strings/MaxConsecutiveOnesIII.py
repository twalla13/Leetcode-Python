# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4595/

from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    #Sliding Window
    #Dynamic window size
    #Constraint Metric: consecutive sequence of 1's with at most k zeros
    #Numeric Metric: max number of consecutive ones
    
    #***Since we are tallying up numbers of ones*** soo we dont need to tally onesss!!!
        # Only need to track # of zeros
        # The window size will give us the max # of consective ones that have at most k zeros
        # when the window has to many zeros we shrink itttttttt
        
    #if we see any more than k zeros in a sequence 
        #then we begin to reduce
    
    #zero tracker
    zeros = 0    
    #max number of consecutive ones
    ans = 0
    
    left = 0
    
    for right in range(len(nums)):
        #print(f"right={right}, left={left}, zeros={zeros}, window_size={right-left+1}")
        
        #build the window by moving right pointer
        if nums[right] == 0: 
            zeros += 1
    
        #while loop removes elements from the left hand side 
        #this shrinks the window until its valid again
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        
        #update the max number of consecutive ones (ans)
        #the size of the window = current length of max consecutive ones that follow the constraint 
        ans = max(ans, right - left + 1)
            
            
    
    return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
result = longestOnes(nums, k)
print(result)