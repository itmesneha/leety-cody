import heapq as h
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        single heap
        '''
        if not lists:
            return None
            
        heap = [] # minheap of size k
        k = len(lists)
        for i, li in enumerate(lists):
            if li:
                h.heappush(heap, [li.val, i, li])

        dummy = ListNode(0)
        cur = dummy
        while heap and cur:
            top = h.heappop(heap)
            i = top[1]
            li = top[2]
            cur.next = li
            if li.next:
                h.heappush(heap, [li.next.val, i, li.next])
            # else:
            #     h.heappush(heap, [li.next.val, i, li.next])
            cur = cur.next

        return dummy.next
