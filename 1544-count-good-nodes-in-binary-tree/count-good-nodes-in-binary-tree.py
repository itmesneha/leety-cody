# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        dfs on left and right keeping track of cur_max
        dfs(node, max(node.val, cur_max))
        '''

        def dfs(node, cur_max):
            if not node:
                return 0

            if node.val >= cur_max:
                res = 1
            else:
                res = 0

            res += dfs(node.left, max(node.val, cur_max))
            res += dfs(node.right, max(node.val, cur_max))

            return res

        return dfs(root, float('-inf'))

