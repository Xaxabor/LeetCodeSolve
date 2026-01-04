# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if  not head.next:
            return None

        c = 0
        temp =head
        while temp:
            temp=temp.next
            c +=1
        if c==n:
            return head.next
        temp= head
        for i in range(c-n-1):
            temp=temp.next
        if n==1:
            temp.next = None
        else:
            temp.next = temp.next.next

        return head