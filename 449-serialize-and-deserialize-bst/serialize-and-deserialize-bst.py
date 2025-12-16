# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.inorder_str = []
        self.preorder_str = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.inorder_str.append(str(node.val)+',')
            inorder(node.right)

        def preorder(node):
            if not node:
                return
            self.preorder_str.append(str(node.val)+',')
            preorder(node.left)
            preorder(node.right)

        inorder(root)
        preorder(root)
        output = ''.join(self.inorder_str) + '*' + ''.join(self.preorder_str)

        # print(output)
        return output
            
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ins, pres = data.split('*')
        inorder = ins.split(',')[:-1]
        preorder = pres.split(',')[:-1]
        # print(inorder)
        # print(preorder)
        inorder = [int(x) for x in inorder]
        preorder =  [int(x) for x in preorder]
        # for c in ins:
        #     inorder.append(int(c))
        # for c in pres:
        #     preorder.append(int(c))
        # print(inorder)
        # print(preorder)

        def build(inorder, preorder):
            if not inorder or not preorder:
                return None
            cur = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            cur.left = build( inorder[:mid], preorder[1:mid+1])
            cur.right = build(inorder[mid+1:], preorder[mid+1:])
            return cur

        return build(inorder, preorder)




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))