# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leftHight(self, node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
            
    def rightHight(self, node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
            
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        lh = self.leftHight(root)
        rh = self.rightHight(root)
        
        if lh == rh:
            return pow(2, lh) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)