# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4598/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # count = 0
        # prev_left = None
        # prev_right = None
        # leftNode = None
        # rightNode = None
        
        # curr = head
        
        # while curr and count < right:
        #     if count == (left - 1):
        #         prev_left = curr
        #         leftNode = curr.next
                
        #     if count == (right - 1):
        #         prev_right = curr
        #         rightNode = curr.next
        #         prev_left = rightNode
        #         prev_right = leftNode
        #         return head
        # curr = curr.next
        # count += 1
        # return head
        
        # count = 1
        
        # curr = head
        # prev_left = None
        # while curr:
        #     print(curr.val, end=" -> ")
        #     curr = curr.next
        #     count += 1
            
        #     if count == (left - 1):
        #         prev_left = curr
        #     elif count == (right - 1):
        #        leftNode = prev_left.next 
        #        prev_left.next = curr.next #right node
        #        curr.next = leftNode #curr node one before right so set the next to the left node
        #        return head
        
        # Create a dummy node to handle edge cases (e.g., reversing from head)
        # dummy.next will always point to the real head of the updated list
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy
        
        #Move prev to the node before the reversal
        for _ in range(left - 1):
            prev = prev.next
            
        # Start reversing nodes between `left` and `right`
        # Example: Input list = 1 → 2 → 3 → 4 → 5, reverse between left=2 and right=4
        # After setup: prev points to node 1, curr points to node 2
        curr = prev.next

        for _ in range(right - left):
            temp = curr.next
            # Example 1st iteration: temp = 3 (node after curr=2)

            curr.next = temp.next
            # Disconnect temp (3) from list: curr (2) now points to 4
            # List becomes: 1 → 2 → 4 → 5, temp = 3

            temp.next = prev.next
            # Point temp (3) to node after prev (prev.next = 2), so temp.next = 2

            prev.next = temp
            # Insert temp (3) after prev (1): now prev.next = 3
            # List becomes: 1 → 3 → 2 → 4 → 5

            # On next iteration:
            # temp = 4, curr = 2 (unchanged)
            # List becomes: 1 → 4 → 3 → 2 → 5
            
        # Return the new head (in case it changed due to reversal at the start)
        return dummy.next