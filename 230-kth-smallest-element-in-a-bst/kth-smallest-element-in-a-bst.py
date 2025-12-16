import heapq as h
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        maintain max_heap of length k
        better - inorder traversal with arr of size k is automatically ascending for BST
        '''
        self.count = 0
        self.ans = 0
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return 
            inorder(node.right)

        inorder(root)
        return self.ans


        # self.max_heap = []
        # def fn(node):
        #     if not node:
        #         return
        #     h.heappush(self.max_heap, -node.val)
        #     if len(self.max_heap) > k:
        #         h.heappop(self.max_heap)

        #     fn(node.left)
        #     fn(node.right)

        # fn(root)
        # return -1 * h.heappop(self.max_heap)