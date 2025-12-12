# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    iterative reverse function(start, end)  + recursive reverseKGroup function
    '''
    def reverse(self, start, end):
        prev, cur = None, start
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #  cur.next = prev
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        start, end = head, head
        for _ in range(k):
            if end == None:
                return head # this group cant be reversed
            end = end.next
        # end is node after required reversing group
        newhead = self.reverse(start, end)
        start.next = self.reverseKGroup(end, k) # end is next node so we'll now start reversing from here
        return newhead


        
                
