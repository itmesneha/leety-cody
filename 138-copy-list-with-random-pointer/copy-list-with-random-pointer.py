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
        '''
        maintain old:new mapping or intervleave nodes
        '''
        if not head:
            return None

        cur, prev = head, head
        dummy = Node(0)
        prev_copy, cur_copy = dummy, dummy
        old_new = {}
        while cur:
            cur_copy = Node(cur.val)
            cur_copy.next = cur.next
            cur.next = cur_copy
            cur = cur.next.next

        # random pointers
        cur = head
        while cur and cur.next:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            else:
                copy.random = None
            cur = copy.next

        # extract new list
        new_head = head.next
        cur = new_head
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return new_head