# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(list1 is None and list2 is None):
            return None
        elif(list1 is not None and list2 is None):
            return list1
        elif(list1 is None and list2 is not None):
            return list2

        head = None
        cur1 = list1
        cur2 = list2

        while(cur1 is not None and cur2 is not None):
            if cur1.val <= cur2.val:
                newNode = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                newNode = ListNode(cur2.val)
                cur2 = cur2.next
            
            if head is None:
                head = newNode
                temp = head
            else:
                temp.next = newNode
                temp = temp.next
        
        while(cur1 is not None):
            newNode = ListNode(cur1.val)
            temp.next = newNode
            temp = temp.next
            cur1 = cur1.next

        while(cur2 is not None):
            newNode = ListNode(cur2.val)
            temp.next = newNode
            temp = temp.next
            cur2 = cur2.next

        return head


        