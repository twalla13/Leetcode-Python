#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow = head
        # fast = head
        
        # while fast:
        #     while slow.val == fast.val:
        #         if fast.next is None: #handles tail case
        #             slow.next = None # duplicates at the end so the last one just points to null 
        #             return head
        #         fast = fast.next #move fast pointer to when slow != fast
        #     slow.next = fast #even if there werent any duplicates this wont change anything bc the fast pointer wont have moved
        #     fast = fast.next #move the fast pointer
        #     slow = slow.next #move slow pointer 
        # return head
        current = head

        # Traverse the list until we reach the end
        while current and current.next:
            if current.val == current.next.val:
                # Skip the next node if it's a duplicate
                current.next = current.next.next
            else:
                    # Only move forward when there's no duplicate
                current = current.next

        return head