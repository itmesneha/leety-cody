"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        cur, prev = head, head
        dummy = ListNode(0)
        prev_copy, cur_copy = dummy, dummy
        old_new = {}
        while cur:
            cur_copy = ListNode(cur.val)
            old_new[cur] = cur_copy # mapping old:new
            prev_copy.next = cur_copy
            prev_copy = cur_copy
            prev = cur
            cur = cur.next

        old = head # old list
        while old:
            new = old_new[old]
            if old.random:
                new.random = old_new[old.random]
            else:
                new.random = None
            
            old = old.next

        return old_new[head]