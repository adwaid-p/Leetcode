# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        if not root:
            return ""
        
        ans = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("N")

        return ','.join(ans)
    
                
    def deserialize(self, data):
        if not data:
            return None
        
        data = data.split(',')
        
        root = TreeNode(int(data[0]))
        q = deque([root])
        
        i = 1
        while q and i < len(data):
            node = q.popleft()

            if i < len(data) and data[i] != 'N':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1

            if i < len(data) and data[i] != 'N':
                node.right = TreeNode(int(data[i]))
                q.append(   node.right)
            i += 1

        return root 

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))