# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p1 = head
        even_head = p1.next
        count = 1 
        while p1.next:
            prev = p1
            count += 1
            temp  = p1.next
            p1.next = temp.next
            p1 = temp

        if count % 2 != 0:
            p1.next = even_head
        else:
            prev.next = even_head

        return head