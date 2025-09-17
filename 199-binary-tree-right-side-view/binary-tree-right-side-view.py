from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        q = deque()
        q.append(root)
        while q:
            rightSide = None
            for _ in range(len(q)):
                cur = q.popleft()
                if cur:
                    rightSide = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if rightSide:
                ans.append(rightSide.val)

        return ans

        # res = defaultdict(list)
        # if not root:
        #     return []

        # def fn(node, level):
        #     if not node:
        #         return
        #     res[level].append(node)
        #     level = level + 1
        #     fn(node.left, level)
        #     fn(node.right, level )
        # fn(root , 1)
        # ans = []
        # for level in res:
        #     ans.append(res[level][-1].val)

        # return ans