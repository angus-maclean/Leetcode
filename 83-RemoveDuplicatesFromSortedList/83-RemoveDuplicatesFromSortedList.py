# Last updated: 02/07/2026, 20:20:33
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start at the head of the list
        current = head
        
        # While current node and its next node are valid
        while current and current.next:
            # Compare current node's value with the next node's value
            if current.val == current.next.val:
                # Skip the duplicate by updating the next pointer
                current.next = current.next.next
            else:
                # Move to the next node if no duplicate
                current = current.next
        
        # Return the modified list
        return head