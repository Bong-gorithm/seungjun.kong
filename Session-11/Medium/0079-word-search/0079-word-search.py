class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w_length = len(word)
        visited = [[False] * n for _ in range(m)]
        
        def dfs(x, y, w_i):
            if w_i == w_length:
                return True

            if  (not (0 <= x < m and 0 <= y < n) 
                    or visited[x][y]
                    or board[x][y] != word[w_i]):
                return False

            visited[x][y] = True

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]: 
                nx = x + dx 
                ny = y + dy

                if dfs(nx, ny, w_i + 1):
                    return True

            visited[x][y] = False
            return False
        
        for i in range(m):
            for j in range(n):
                 if dfs(i, j, 0):
                    return True

        return False                    