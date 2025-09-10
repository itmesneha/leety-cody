# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        if not head:
            return head
        if not head.next:
            return None

        cur = head
        while cur:
            count += 1
            cur = cur.next

        middle = floor(count/2)
        # print('middle: ', middle)
        pos = 0
        cur = head
        while pos != middle:
            # print('pos: ', pos)
            pos += 1
            prev = cur
            cur = cur.next

        prev.next = cur.next
        cur.next = None

        return head

