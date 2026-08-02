from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0

        visited = [[False for _ in range(m)] for _ in range(n)]
        que = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append([[i, j], 0])
                    visited[i][j] = True

        while que:
            [i, j], time = que.popleft()

            ans = max(ans, time)

            if i - 1 >= 0 and not visited[i - 1][j] and grid[i - 1][j] == 1:
                que.append([[i - 1, j], time + 1])
                visited[i - 1][j] = True

            if i + 1 < n and not visited[i + 1][j] and grid[i + 1][j] == 1:
                que.append([[i + 1, j], time + 1])
                visited[i + 1][j] = True

            if j - 1 >= 0 and not visited[i][j - 1] and grid[i][j - 1] == 1:
                que.append([[i, j - 1], time + 1])
                visited[i][j - 1] = True

            if j + 1 < m and not visited[i][j + 1] and grid[i][j + 1] == 1:
                que.append([[i, j + 1], time + 1])
                visited[i][j + 1] = True

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    return -1

        return ans
