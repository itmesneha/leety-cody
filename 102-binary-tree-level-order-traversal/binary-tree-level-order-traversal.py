# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        if not root:
            return ans
        q.append(root)
        # print('q: ', q)
        while q:
            li = []
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft()
                li.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # print('q: ', q)
            ans.append(li)
            # print('ans: ', ans)

        return ans