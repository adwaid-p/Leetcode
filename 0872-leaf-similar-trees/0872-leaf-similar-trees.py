# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafNode1 = []
        leafNode2 = []
        
        def dfs(root, leafNodes):
            if not root:
                return
            if root.left is None and root.right is None:
                leafNodes.append(root.val)
                return
            dfs(root.left, leafNodes)
            dfs(root.right, leafNodes)

        dfs(root1, leafNode1)
        dfs(root2, leafNode2)

        return leafNode1 == leafNode2