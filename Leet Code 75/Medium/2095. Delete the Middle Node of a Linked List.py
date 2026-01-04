# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None 
        if head.next and not head.next.next:
            head.next = None
            return head

        prevslow=None
        fast=head
        slow=head

        while fast and fast.next:
            prevslow= slow      # 0 1 2
            slow = slow.next    # 1 2 3
            fast=fast.next.next # 2 4 6

        prevslow.next = prevslow.next.next

        return head