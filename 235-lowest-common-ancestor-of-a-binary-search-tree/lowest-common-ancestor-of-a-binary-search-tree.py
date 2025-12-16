# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        larger = max(p.val, q.val)
        smaller = min(p.val, q.val)

        while root:
            if root.val > larger:
                root = root.left
            if root.val < smaller:
                root = root.right
            if smaller <= root.val <= larger:
                return root

