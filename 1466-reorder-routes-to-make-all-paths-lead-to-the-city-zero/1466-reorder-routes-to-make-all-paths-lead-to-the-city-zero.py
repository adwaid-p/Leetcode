from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for city1, city2 in connections:
            adj[city1].append((city2, 1))
            adj[city2].append((city1, 0))
        
        total_flip = 0

        queue = deque([0])
        visited = [False] * n
        visited[0] = True

        while queue:
            current_city = queue.popleft()

            for neighbor, direction in adj[current_city]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    total_flip += direction
                    queue.append(neighbor)
            
        return total_flip