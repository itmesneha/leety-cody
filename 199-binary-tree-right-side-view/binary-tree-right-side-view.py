# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        ans = []
        if not root:
            return ans
        
        q.append(root)
        
        while q:
            qlen = len(q)
            for i in range(qlen):
                cur = q.popleft()
                rightside = cur
                # if i == qlen -1:
                #     ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            # ans.append(q.popleft().val)
            ans.append(rightside.val)

        return ans

