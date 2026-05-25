from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        visited = [[False] * n for _ in range(m)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True

            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == "1" and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    bfs(i, j)
                    count += 1 

        return count