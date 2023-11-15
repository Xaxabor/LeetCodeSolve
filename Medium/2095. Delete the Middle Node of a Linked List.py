# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        i, count = 0, 0
        while(temp is not None):
            temp = temp.next
            count +=1

        if count == 1:
            return None
        
        temp = head
        while(i<(count//2)-1):
            temp = temp.next
            i = i+1
        
        temp.next = temp.next.next

        return head

