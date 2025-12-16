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
        ans = []
        # ans.append(root.val)
        def dfs(node, cur_max):
            if not node:
                return 

            if node.val >= cur_max:
                ans.append(node.val)
            
            dfs(node.left, max(node.val, cur_max))
            dfs(node.right, max(node.val, cur_max))

        dfs(root, float('-inf'))
        # print('ans: ', ans)
        return len(ans)

