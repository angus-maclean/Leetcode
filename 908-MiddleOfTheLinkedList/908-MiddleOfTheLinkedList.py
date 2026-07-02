# Last updated: 02/07/2026, 20:20:18
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start a fast and slow pointer
        slow, fast = head, head
        
        # while the pointer is still valid
        while fast and fast.next:
            # increment the pointers
            slow = slow.next
            fast = fast.next.next
        return slow

            
        # if the length of the list is even then return slow.next
        # if the length of the list is odd return slow
        
        
        