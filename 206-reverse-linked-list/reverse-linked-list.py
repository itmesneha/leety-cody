# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(me):
            if not me or not me.next:
                return me
            friend = me.next
            newHead = rev(friend)
            me.next = None
            friend.next = me
            return newHead
        return rev(head)