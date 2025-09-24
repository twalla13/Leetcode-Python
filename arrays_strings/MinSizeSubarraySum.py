# https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=ajc81mgt

# Sliding Window
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    #Sliding window bc valid subarray must sum to target 
    #Dynamic window size 
    #Length of subarray = right - left + 1
    
    left = curr = 0
    ans = float ('inf') #very large number 
    for right in range(len(nums)):
    
        curr += nums[right]
        print('current sum', curr, "window size", right - left + 1)
            
        #need a while loop bc need to shrink window until its valid again
        while curr >= target: #shrink window, curr is too large
            #cur >= target is a valid subarray so we need to check if its the smallest so far
            #Need to check first bc once we move left we dont know if its a valid subarray 
            ans = min(ans, right - left + 1)
            curr -= nums[left]
            left += 1

             
            print('current sum ', curr, "ans ", ans)
    return 0 if ans== float('inf') else ans
target = 11
nums = [1,2,3,4,5]
print(minSubArrayLen(target, nums))