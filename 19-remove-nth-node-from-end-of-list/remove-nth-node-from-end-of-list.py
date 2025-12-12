# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        take a pointer to end keep count of total
        take another one to correct
        '''
        cur = head
        if not head or not head.next:
            return None
        count = 0
        while cur:
            count += 1
            cur = cur.next
        print('count: ', count)
        to_delete = count - n # 0 - index
        cur = head
        dummy_head = ListNode(0)
        dummy_head.next = cur
        prev = dummy_head
        index = 0
        while index != to_delete:
            prev = cur
            cur = cur.next
            index += 1
        prev.next = cur.next
        cur.next = None
        return dummy_head.next