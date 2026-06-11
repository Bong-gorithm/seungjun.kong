class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        def dfs(x, y):
            # 이미 계산한 칸
            if dp[x][y] != 0:
                return dp[x][y]

            dp[x][y] = 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] > matrix[x][y]:
                        dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))

            return dp[x][y]

        answer = 0

        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))

        return answer