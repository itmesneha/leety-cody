# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return 0
        leftDepth = self.height(root.left)
        rightDepth = self.height(root.right)
        return 1 + max(leftDepth, rightDepth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        leftDepth = self.height(root.left)
        rightDepth = self.height(root.right)
        if abs(leftDepth - rightDepth) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        