# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        reverse second half of list
        then merge node by node
        """
        if not head or not head.next:
            return None
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # print('slow: ', slow) # middle node
        middle = slow
        prev.next = None
        # print('prev: ', prev)

        def reverse(me):
            if not me.next:
                return me
            fren = me.next
            newhead = reverse(fren)
            fren.next = me
            me.next = None
            return newhead

        second_half_head = reverse(middle)
        # print('second_half_head: ', second_half_head)

        while head and second_half_head:
            t1 = head.next
            t2 = second_half_head.next
            head.next = second_half_head
            if t1:
                second_half_head.next = t1
            second_half_head = t2
            head = t1

        return 
        