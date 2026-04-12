# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(node, currentSum, path):
            if not node:
                return
                
            path.append(node.val)
            currentSum += node.val

            if node.left is None and node.right is None and currentSum == targetSum:
                paths.append(path[:])
            
            dfs(node.left, currentSum, path)
            dfs(node.right, currentSum, path)
            
            path.pop()
        
        dfs(root, 0, [])
        return paths