# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
    cannot use inorder + preorder trick as there are duplicates
    can use any traversal except inorder as dont know root in it
    using preorder here with nulls.
    for deserialize keep index moving 1 forward.
    Read values in preorder; on None return null, otherwise build node → left → right.
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []

        def preorder(node):
            if not node:
                self.res.append('None')
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
        preorder = data.split(',')
        self.i = 0
        # print(preorder)

        def build():
            if preorder[self.i] == 'None':
                self.i += 1
                return None

            cur = TreeNode(int(preorder[self.i]))
            self.i += 1
            
            cur.left = build()
            cur.right = build()
            return cur

        return build()




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))