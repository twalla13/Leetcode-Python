#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/


from collections import Counter
from typing import List


def largestUniqueNumber(nums: List[int]) -> int:
    
    nums_count = Counter(num for num in nums)
    currMax = -1
    for num, count in nums_count.items():
        if count == 1 and num > currMax:
            currMax = num
    return currMax
    
nums = [5,7,3,9,4,9,8,3,1]
print(largestUniqueNumber(nums))