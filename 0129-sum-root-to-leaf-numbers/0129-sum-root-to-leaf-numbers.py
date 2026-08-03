# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumPath(node, num):
            if not node:
                return 0
            
            num += str(node.val)

            if not node.left and not node.right:
                return int(num)
            
            left = sumPath(node.left, num)
            right = sumPath(node.right, num)

            return left + right

        return sumPath(root,'')