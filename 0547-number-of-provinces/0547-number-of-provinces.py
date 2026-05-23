class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(i):
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and j not in self.visited:
                    dfs(j)
        
        self.visited = set()
        provinces = 0
        n = len(isConnected)

        for i in range(n):
            if i not in self.visited:
                provinces += 1
                dfs(i)
        
        return provinces