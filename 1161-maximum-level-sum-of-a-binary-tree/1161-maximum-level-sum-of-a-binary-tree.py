# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        #no need of checking empty tree becasuse this problem guarantees a non-empty tree.
        queue = deque([root])

        level = max_level = 0
        max_level_sum = float('-inf')

        while queue:

            level += 1

            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
        
        return max_level