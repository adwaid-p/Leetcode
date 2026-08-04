# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []

        def dfs(node, targetSum, path):
            if not node:
                return
            path.append(node.val)
            targetSum -= node.val

            if not node.left and not node.right and targetSum == 0:
                result.append(path[:])
            
            dfs(node.left, targetSum, path)
            dfs(node.right, targetSum, path)
            path.pop()
        
        dfs(root, targetSum, [])

        return result