# https://leetcode.com/problems/two-sum/submissions/1751722865/
# Hashing 
from collections import defaultdict


def twoSum(nums: List[int], target: int) -> List[int]:
        #Need to make element to index
        #Key fact: compliment = target - element

        #loop through array
        #while looping check if the compliment with the current element exists in hashmap already if so return the current index and the map[compliment]

        mapping = defaultdict(int)
        result = []
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in mapping:
                result.append(i)
                result.append(mapping[compliment])
                return result
            else:
                mapping[nums[i]] = i
        