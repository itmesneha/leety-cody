# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        if not head or not head.next:
            return None

        # count length
        cur = head
        while cur:
            count += 1
            cur = cur.next

        middle = count // 2

        cur = head
        for _ in range(middle - 1):
            cur = cur.next

        cur.next = cur.next.next
        
        return head

