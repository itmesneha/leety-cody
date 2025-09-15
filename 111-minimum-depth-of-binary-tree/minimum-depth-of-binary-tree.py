from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append((root,1))
        while q:
            cur, depth = q.popleft()
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                q.append((cur.left, depth + 1))
            if cur.right:
                q.append((cur.right, depth + 1))
        
        # def fn(cur):
        #     if not cur:
        #         return float('inf') # invalid path
        #     if not cur.left and not cur.right:
        #         return 1
        #     return 1 + min(fn(cur.left), fn(cur.right))

        # return fn(root)