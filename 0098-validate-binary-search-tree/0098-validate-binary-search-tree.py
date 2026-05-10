# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True

        def validate(node, lower, higher):
            if not node:
                return

            if node.val > lower and node.val < higher:
                self.ans &= True
            else:
                self.ans &= False

            validate(node.left, lower, node.val)
            validate(node.right, node.val, higher)

            

        lower = float('-inf')
        higher = float('inf')
        validate(root, lower, higher)
        return self.ans