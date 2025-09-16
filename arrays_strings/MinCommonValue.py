# https://leetcode.com/problems/minimum-common-value/?envType=problem-list-v2&envId=ajc81mgt
from typing import List


def getCommon(nums1: List[int], nums2: List[int]) -> int:
    # two pointer for both arrays since they are both in increasing
        # 1 2 3
        # ^
        # 2 4
        # ^
    i = 0
    j = 0

    # loop throught the shortest array
    while i < len(nums1) and j < len(nums2):
        
        print(nums1[i], ",", nums2[j])
        if nums1[i] == nums2[j]:
    
                # only need to return on bc they are same
                return nums1[i]
            
        elif nums1[i] < nums2[j]:
                # we can move i bc nums[1] and we are increasing order
            i += 1
        else:
            j += 1
            
    #Once either pointer reaches the end, no more comparison is possible, so you should just return -1
    
    # while i < len(nums1):
    #     if nums1[i] == nums2[j]:
    #         # only need to return on bc they are same
    #         return nums1[i]
    #     i += 1
    # while j < len(nums2):
    #     if nums1[i] == nums2[j]:
    #     # only need to return on bc they are same
    #         return nums1[i]
    #     j += 1  
            
    return -1
nums1 = [1,1,2]
nums2 = [2,4]
print(getCommon(nums1, nums2))