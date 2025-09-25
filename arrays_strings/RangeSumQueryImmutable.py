#https://leetcode.com/problems/range-sum-query-immutable/description/?envType=problem-list-v2&envId=ajc81mgt


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
    def sumRange(self, left: int, right: int) -> int:
        #two pointers fo'sure
        #nums is a list of ints 
        #left and right are on opposite ends of input
        ans = 0
        while left <= right:
            ans += self.nums[left]
            
            left += 1
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)