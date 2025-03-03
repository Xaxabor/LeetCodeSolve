# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp is None or temp.next is None:
            return head
        while(temp is not None):
            if temp.next is None:
                break
            if temp.val == temp.next.val :
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
