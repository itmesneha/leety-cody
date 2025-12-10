# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        recursion
        '''
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


        # 2 pointer
        # '''
        # p1 = list1
        # p2 = list2
        # head = ListNode()
        # cur = head
        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         cur.next = p1
        #         p1 = p1.next
        #     else:
        #         cur.next = p2
        #         p2 = p2.next

        #     cur = cur.next

        # if p1:
        #     cur.next = p1
        
        # if p2:
        #     cur.next = p2

        # return head.next

        