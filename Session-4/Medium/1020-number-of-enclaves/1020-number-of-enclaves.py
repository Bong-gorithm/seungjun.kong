from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        m, n = len(grid), len(grid[0])
        def check_island(a, b):
            queue = deque()
            queue.append((a, b))
            grid[a][b] = 0

            cnt = 1 
            is_island = True
            while queue:
                x, y = queue.popleft()

                if x == m - 1 or y == n - 1 or x == 0 or y == 0:
                    is_island = False

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 0
                        cnt += 1
            
            return cnt if is_island else 0
        
        output = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    output += check_island(i, j)

        return output