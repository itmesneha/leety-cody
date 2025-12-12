# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        find left height, right height, keep ans max as left + right
        dont forget to return the height in the recursive function
        '''
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            ans = max(ans, left_height + right_height) # no +1 here because height counts nodes and we want to count edges
            return 1 + max(left_height, right_height)

        helper(root)
        return ans