# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        3 options: only root good, left or right good, left + right + root good
        take max of all 3 for ans
        but return only max of (only root good, left or right good) in recursion to
        propagate upwards
        '''
        self.ans = float('-inf')
        def fn(node):
            if not node:
                return 0
            left = fn(node.left)
            right = fn(node.right)

            only_root_good = node.val
            left_or_right_good = max(left, right) + node.val
            current_good = left + right + node.val

            self.ans = max(self.ans, only_root_good, left_or_right_good ,current_good )
            return max(only_root_good ,left_or_right_good)

        fn(root)
        return self.ans