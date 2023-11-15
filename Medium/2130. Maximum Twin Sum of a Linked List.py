# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = list()
        slow = head
        fast = head

        while(fast):
            l.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        i = -1
        m = 0
        s = 0
        while(slow):
            s = slow.val + l[i]
            if s>m:
                m = s
            i = i-1
            slow = slow.next

        return m
        