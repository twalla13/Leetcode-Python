#https://leetcode.com/problems/find-lucky-integer-in-an-array/?envType=problem-list-v2&envI

#Hashing, Counter

from collections import Counter
from typing import List


def findLucky(arr: List[int]) -> int:
    numsCount = Counter(arr)
    
    ans = -1
    
    
    #For counter need to iterate over key-value pairs
    for value, freq in numsCount.items():
        if value == freq:
            ans = max(ans, value)
    return ans


arr = [2,2,3,4]
print(findLucky(arr))