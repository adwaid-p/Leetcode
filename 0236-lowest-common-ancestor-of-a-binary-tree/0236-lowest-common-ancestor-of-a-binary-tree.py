# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pList = []
        self.qList = []

        def dfs(root, tempList):
            if not root:
                return
 
            tempList.append(root)

            if root == p:
                self.pList = tempList.copy()
            if root == q:
                self.qList = tempList.copy()
            
            dfs(root.left, tempList)
            dfs(root.right, tempList)

            tempList.pop()
        
        dfs(root, [])

        qSet = set(self.qList)
        result = [node for node in self.pList if node in qSet]

        return result[-1] 
