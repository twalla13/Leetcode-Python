#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4845/

from collections import defaultdict
from typing import List


def findMaxLength(nums: List[int]) -> int:
     #Sliding window wont work here bc as soon as I widen the winnow I cant guarantee I'lll shrink back to balanced zeros and ones counts
     #Sliding window only works when the condition is monotonic (strictly increase or decreasing) as the windows grows or shrinks
        #Examples of monotonic:
            #Window sum <= K : when we add an element and break the constraint we know we can safely shrink from the left until it holds again
            #Window has at most distinct K chars : can incrementally add/drop and maintain counts 
    
    #EXACTLY same count A and B is NOT MONOTONIC
        # Adding a new element can swing your balance from 0 to ±1 or more.
        # Shrinking from the left can swing it unpredictably.
        # There’s no “once it’s balanced, growing makes it unbalanced in just one direction” guarantee.
        
    #Any time you see exactly switch gears to prefix sums + hashmap trick 
        #Maintain running sum as you scan
        #Remember the earliest index each sum value appeared
        #When you see the same running sum again, you know the elements in between net to zero, so you can compute their length in O(1).
        
    """
    Return the length of the longest subarray with equal numbers of 0s and 1s.
    We treat 0 as –1 and 1 as +1 so that a zero-sum subarray means balance.
    """
    # This dictionary maps each running sum value to the first index we saw it at
    # You record the earliest index for each running sum because that gives you the longest possible subarray when you see that same sum again. 
    # first_seen maps sum value (prefix sum of zeros(-1) and ones (+1)) -> first index we saw it at
    first_seen = {0: -1}     # “sum 0” effectively starts just before index 0
    running = 0              # our cumulative sum as we scan (prefix sum)
    best = 0                 # the longest balanced span found so far
    
    
    for i, val in enumerate(nums):
        # Convert 0→–1, 1→+1 and update our running total
        # Running total is prefix sum
        # At each real index i, we update running by +1 or –1.
        if val == 0:
            running -= 1
        else:  # val == 1
            running += 1
            
        # If we’ve seen this running sum before, subarray between then and now sums to zero
        if running in first_seen:
            # length = current_index – index_when_we_first_saw_this_sum
            length = i - first_seen[running]
            # update best if this span is longer
            if length > best:
                best = length
        else:
            # first time seeing this running sum: record the index
            first_seen[running] = i

    return best 
nums = [0,1,1,1,1,1,0,0,0]

print(findMaxLength(nums))