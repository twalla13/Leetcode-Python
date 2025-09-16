#https://leetcode.com/problems/find-pivot-index/?envType=problem-list-v2&envId=ajc81mgt
#Array_strings Prefix Sum


def pivotIndex(self, nums: List[int]) -> int:
        # Prefix sum fo'sure
        # nums: [1, 7,3, 6, 5, 6]
        # Pref: 1, 8,11,17,22,28
        # if I want sum of nums[3:5] I do...
            #prefix[5] - prefix[3]
            # 28 - 17 = 11

        # prefix array indices match nums indices
        # but need a way to track prefix sums to see if we have an equal on -> set?
        # But the pivot index has nothing to do with whether either sum was seen before. That condition could be true due to values at other indices — which isn’t what you want. You care about a very specific moment: does left side equal right side right now at index i?



    # we’re not looking for a place where the left sum ever was equal to the right sum at some other index. We only care whether they are equal right now at the current index.

        left_sum = 0
        # sums = []
        total = sum(nums)
        #you were You were skipping the last index by looping to len(nums) - 1
        for i in range(len(nums)):
            #You’re comparing the sum to the right of i as total - left_sum, but left_sum already includes nums[i], so you’re off by one. NEED to subtract nums[i] bc STRICTLY RIGHT 
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i] #calculate prefix on the fly

        return -1
    
nums = [2,1,-1]
print(pivotIndex(nums))