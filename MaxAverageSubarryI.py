#https://leetcode.com/problems/maximum-average-subarray-i/

from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    # Average will n1 + n2 + n3 + n4 + Nk .... / k
        # Window is equal to K
        # max = 0
            # if max > current avg then max = current avg 

        #if length > k, exist

        # #Code
        # max = float('-inf') 
        # left = 0
        # right = k-1

        # while right < len(nums):
            
        #     temp = left
        #     sum = 0
        #     #sums all indices in window using the right pointer as a sentinel
        #     while temp <= right:
        #         print("current number", nums[temp])
        #         sum += nums[temp] 
        #         print("current sum", sum)
        #         temp += 1
            
        #     #find the avd
        #     current_avg = sum / k

        #     print("current avg: ", current_avg) 
        #     if current_avg > max:
        #         max = current_avg

        #     left += 1
        #     right += 1

        # return max
        
        #initial window and sum average
        #this covers the first window so when we start the loop we need to start one over
        window_sum = sum(nums[:k])
        max_avg = window_sum / k
        
        #slide window across array
        #so we did the first window and we are going to loop from k to len(nums)
        for right in range(k, len(nums)):
            left = right-k
            #remove element from left (-nums[left])
            #add element on right (+nums[right])
            window_sum += nums[right] - nums[left]
            
            #find current avg of new window
            current_avg = window_sum / k
            
            #check if its greater than current
            if max_avg < current_avg:
                max_avg = current_avg
                
        return max_avg
            
    

nums = [1,12,-5,-6,50,3]
result = findMaxAverage(nums, 4)
print(result)