# Monotonic Stack

# https://leetcode.com/problems/next-greater-element-i/description/

from typing import List


#
# Problem: Find the next greater element for each element in nums1 from nums2
# Strategy: Use a monotonic decreasing stack to build a map of next greater elements in nums2
#
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # next_greater = {}
        # ans = [-1] * len(nums1)
        # for i in range(len(nums2)):
        #     if not stack or stack[-1] >= nums2[i]: #if stack empty or top of stack >= current i
        #         stack.append(nums2[i])
        #     while  i < len(nums2) and stack and stack[-1] < nums2[i]: #while stack not empty and top of stack < current i
        #         temp = stack.pop() #found next greater, pop off
        #         stack.append(nums2[i])
                
        #         next_greater[temp] = nums2[i] # add to map top of stack -> next greater (current i)
        #         i += 1
        
        #     print("stack",stack)
        # print("next greater",next_greater)
        # for i in range(len(nums1)): #must iterate through nums1 to maintain order by index
        #     if nums1[i] in next_greater: #check if next greater exists in map
        #         ans[i] = next_greater[nums1[i]]
        #     print(ans)
        # return ans
    
    stack = []  # This stack helps us track decreasing elements from nums2
    nextgreater = {}  # Dictionary to map each number to its next greater number
    ans = []  # Final result list for each num in nums1

    # Iterate through nums2 to build the nextgreater mapping
    for num in nums2:
        while stack and num > stack[-1]:  # While the current number is greater than the top of the stack
            prev = stack.pop()  # This means we found the next greater element for 'prev'
            nextgreater[prev] = num  # Map 'prev' to current num
        stack.append(num)  # Push the current num to stack

    # Iterate through nums1 and lookup each number in the nextgreater map
    for num in nums1:
        ans.append(nextgreater.get(num, -1))  # Use -1 if no greater element exists
    # Return the result list
    return ans
    
nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
result = nextGreaterElement(nums1, nums2)
print(result)