#https://leetcode.com/problems/contains-duplicate/description/
from ast import List


def containsDuplicate(nums: List[int]) -> bool:
        #use the set function in python, will only keep unique elements
        #if the newSet equals the nums then return false (no dupilcates)

        # mySet = set(nums)
        # newList = list(mySet)

        # if newList == nums:
        #     return False
        
        # return True


        # #You only need to know if any value repeats. You don’t care about order. A reliable check is:
        # return len(nums) != len(set(nums))
    
    #Better time complexity
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                return True
        return False