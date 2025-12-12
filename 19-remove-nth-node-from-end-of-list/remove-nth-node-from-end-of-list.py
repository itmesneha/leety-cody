# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        take first and second pointers with a difference of n (n nodes between them)
        + first, second points to dummy node 
        '''
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n+1):
            second = second.next # now gap of n nodes between first & second

        while second:
            second = second.next
            first = first.next 

        first.next = first.next.next

        return dummy.next