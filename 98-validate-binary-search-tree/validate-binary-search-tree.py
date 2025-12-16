# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # limit_left = how big it can be
        # limit_right = how small it can be
        def fn(root, high, low):
            if not root:
                return True

            if not low < root.val < high:
                return False
            
            # if root.left and (root.left.val >= root.val or root.left.val >= limit_left):
            #     return False

            # if root.right and (root.right.val <= root.val or root.right.val <= limit_right):
            #     return False

            return fn(root.left, root.val, low) and fn(root.right, high, root.val)

        return fn(root, float('inf'), float('-inf'))