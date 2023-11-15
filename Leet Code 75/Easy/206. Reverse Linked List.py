# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            
            prev = None
            current = head
            while(current.next is not None):
                upcoming = current.next
                current.next = prev
                prev = current
                current = upcoming
            current.next = prev

            return current





        