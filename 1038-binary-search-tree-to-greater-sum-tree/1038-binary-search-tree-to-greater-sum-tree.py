# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, currSum):
            if not node:
                return currSum
            
            currSum = dfs(node.right, currSum)

            currSum += node.val
            node.val = currSum 

            currSum = dfs(node.left, currSum)

            return currSum
        
        dfs(root, 0)
        return root