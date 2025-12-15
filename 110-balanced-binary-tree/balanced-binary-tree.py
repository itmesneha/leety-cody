# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fn(self, node):
        '''
        Checks if a binary tree is height-balanced using a single DFS traversal.
        Each recursive call returns a tuple (is_balanced, height), allowing early
        termination when an unbalanced subtree is found.
        Time: O(n), Space: O(h)
        '''
        if not node:
            return True, 0

        left_balanced, left_depth = self.fn(node.left)
        if not left_balanced:
            return False, 0

        right_balanced, right_depth = self.fn(node.right)
        if not right_balanced:
            return False, 0

        if abs(left_depth - right_depth) > 1:
            return False, 0

        return True, 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.fn(root)[0]