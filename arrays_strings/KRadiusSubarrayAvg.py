#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4836/

from typing import List


def getAverages(nums: List[int], k: int) -> List[int]:
    """
        Can solve with sliding window over a fixed width (2*k + 1)
    """
    
    #We know the window size is 2 * K but need to add 1 since starting array at zero
    windowSize = 2*k + 1
    n = len(nums)
    
    ans = [-1] * n #create an array with length n and filled with -1
    
    if n < windowSize: #length of array is to small to have a k radius, no center has enough radius
        return -1
    
    #initialize first window sum 
    windowSum = sum(nums[0:windowSize]) # nums[0:w] slices the array from nums[0] to right before nums[w]
    
    # the kth index in the answer array is equal to the first window sum 
    # First full window with center at k / window size for the avg
    ans[k] = windowSum // windowSize #ensures k has a valid window
    
    for i in range(k, n):
        # add new right element nums[i + k] but must ensure right is in bounds
        # remove left element [i - k - 1], need the -1 since window size is 2k + 1
        if i + k < n :
            windowSum += nums[i+k] - nums[i-k-1]
            ans[i] = windowSum // windowSize
        
    
    #return ans

    """
        Prefix Sum Solution
    """
    
    #build prefix array
    n = len(nums)
    prefix = [nums[0]]
    windowSize = 2*k + 1
    ans = [-1] * n
    if n < windowSize : #length of array smaller than diameter  = 2k + 1
        return ans
    
    for i in range(1,n):
        prefix.append(nums[i] + prefix[-1])
    
    
    
    for i in range(k, n):
         if i + k < n : #ensure right is in bounds
            left = i-k-1 
            #since i-k-1 can be negative when i == k, you also handle that by using a conditional:
            leftSum = prefix[left] if left >= 0 else 0 #ensure left is in bounds
            windowSum = prefix[i+k] - leftSum
            ans[i] = windowSum // windowSize
    
    return ans

# Call the function and print the result
result = getAverages([100000],0)
print(result)  