from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        visited = [[False] * n for _ in range(m)]

        def bfs(x, y) -> List:
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True

            visited_dots = [(x, y)]
            is_surrounded = True

            while queue:
                x, y = queue.popleft()

                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    is_surrounded = False

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == "O" and not visited[nx][ny]:
                            visited[nx][ny] = True
                            visited_dots.append((nx, ny))
                            queue.append((nx, ny))

            return visited_dots if is_surrounded else []

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    visited_dots = bfs(i, j)

                    for x, y in visited_dots:
                        board[x][y] = "X"
        
        return board