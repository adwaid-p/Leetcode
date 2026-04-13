# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, currentSum, prefix_map):
            if not node:
                return 0

            currentSum += node.val
            target = currentSum - targetSum

            count = prefix_map.get(target, 0)
            
            prefix_map[currentSum] = prefix_map.get(currentSum, 0) + 1

            count += dfs(node.left, currentSum, prefix_map)
            count += dfs(node.right, currentSum, prefix_map)

            prefix_map[currentSum] -= 1
            currentSum -= node.val

            return count
        
        return dfs(root, 0, {0: 1})