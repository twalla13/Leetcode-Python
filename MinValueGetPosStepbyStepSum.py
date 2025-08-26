# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4657/

from typing import List


def minStartValue(nums: List[int]) -> int:
     
    # #build prefix sum 
    # #can add starting value to prefix sum array to get (step by step value + startValue)
     
    # prefix = [nums[0]]
    # smallestElement = nums[0]

    # startValue = 0
    # for i in range(1, len(nums)):
    #     prefix.append(nums[i] + prefix[-1])
    #     #Need to make an educated guess as to what the min value could be
    #     #find the smallest element in prefix 
    #     if prefix[i] <  smallestElement:
    #         smallestElement = prefix[i]
            
    #     # # we want startValue + smallestElement >= 1
    #     # # algebra gives us startValue >= 1 - smallestElement
    #     # startValue = 1 - smallestElement
    #     # #if the 1 - smallest element is zero 
    #     #     # Mathematically every “step sum” (0+1, 0+3) stays ≥ 1, so your logic thinks 0 is enough.
    #     # if 1 - smallestElement == 0:
    #     #     startValue = 1
    
            
    #     # #find the current prefix sum with startValue
    #     # currentSum = startValue + prefix[i] 
    #     # #only increase startValue when currentSum < 1
    #     # if currentSum < 1:
    #     #     startValue +=1
    #         # compute minimum startValue so that startValue + min_prefix >= 1
            
    #     # if smallestElement >= 1, starting at 1 suffices; otherwise shift up by (1 - smallestElement)
    #     startValue = 1 if smallestElement >= 1 else 1 - smallestElement
    # return startValue
    
    """
        Find the min pos startValue such that running total of 
        startValue + runningSum >= 1
    """
    
    #Initialize current sum and minimum prefix amount as the first element in the nums array
    #build prefix sum 
    #can add starting value to prefix sum array to get (step by step value + startValue)
    curr_sum = nums[0]
    
    min_prefix = curr_sum #smallest prefix sum
    

    #build prefix sum and track the smallest prefix sum
    for num in nums[1:]:
        curr_sum += num
        #Need to make an educated guess as to what the min value could be
        #find the smallest element in prefix 
        if curr_sum < min_prefix:
            min_prefix = curr_sum
    
    
    #if the smallest prefix is already >=1, startValue is 1
    #otherwise, startValue + min_prefix = 1 ----> startValue = 1 - min_prefix
    return 1 if min_prefix >= 1 else 1 - min_prefix
nums = [-3,2,-3,4,2]
result = minStartValue(nums)
print(result)