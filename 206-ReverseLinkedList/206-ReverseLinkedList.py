# Last updated: 02/07/2026, 20:20:28
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        # we need:
        # previous, curret, nextnode

        # the head does not have a  prev
        prev = None
        # we start at the head (first node)
        current = head
        # while current is valid node
        while current:
            nextnode = current.next # keep track of the next node
            current.next = prev # reverse direction of the pointer
            prev = current # set current node which will be prev for the next pointer
            current = nextnode # move the current pointer along
        return prev

