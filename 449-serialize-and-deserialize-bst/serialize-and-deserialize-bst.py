# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    to use bst property, encode to preorder without nulls then use build(low, high)
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []

        def preorder(node):
            if not node:
                return 

            self.res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        output = ','.join(self.res)

        # print(output)
        return output
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder = data.split(',')
        self.i = 0
        # print(preorder)
        n = len(preorder)
        def build(low, high):
            if self.i >= n:
                return None

            val = int(preorder[self.i])
            if not low < val < high:
                return None

            cur = TreeNode(val)
            self.i += 1
            
            cur.left = build(low, cur.val)
            cur.right = build(cur.val, high)
            return cur

        return build(float('-inf'), float('inf'))




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))