#https://leetcode.com/problems/sum-of-unique-elements/description/?envType=problem-list-v2&envId=ajcqwr0m


#Hashing, Counter

from collections import Counter
from typing import List


def sumOfUnique(nums: List[int]) -> int:
    #sum all the unique elements
    # 1 2 3 2 
    # set -> 1, 2 , 3
    # sum the set? No only returns list without duplicates not unique ones
    
    # Sum the elements with freq of 1 
    numsCount = Counter(nums)
    ans = 0
    for num, freq in numsCount.items():
        if freq == 1:
            ans += num
    return ans
nums = [1,2,3,2]

print(sumOfUnique(nums))