# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None) or (head.next.next is None):
            return head

        odd = head
        temp = head.next
        even = head.next

        while(odd is not None and even is not None):
            odd.next = odd.next.next
            odd = odd.next
            if(even.next is not None):
                even.next = even.next.next
                even =  even.next

        
        odd  = head
        while odd.next is not None:
            odd = odd.next
        
        odd.next = temp
            
        return head