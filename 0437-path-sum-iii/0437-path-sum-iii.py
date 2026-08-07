# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths = 0        

        def dfs(node, resultPath):
            if not node:
                return 0
            
            resultPath.append(node.val)

            i = len(resultPath) - 1
            currSum = 0
            while i >= 0:
                currSum += resultPath[i]
                if currSum == targetSum:
                    self.paths += 1
                i -= 1
            
            dfs(node.left, resultPath)
            dfs(node.right, resultPath)
            resultPath.pop()
        
        dfs(root, [])
        return self.paths