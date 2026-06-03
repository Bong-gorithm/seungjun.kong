from collections import deque

'''
- 태평양 → 1
- 대서양 → 2
- 미방문 → 0
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = (len(heights), len(heights[0]))
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        visited = [[[0, 0] for _ in range(n)] for _ in range(m)]
        queue = deque()
        def bfs(w):
            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < m and 0 <= ny < n:
                        if visited[nx][ny][w] == 0 and heights[x][y] <= heights[nx][ny]:
                            visited[nx][ny][w] = 1
                            queue.append((nx, ny))

        # 태평양 방문 여부 처리
        for i in range(m):
            visited[i][0][0] = 1
            queue.append((i, 0))
        for j in range(n):
            visited[0][j][0] = 1
            queue.append((0, j))
        bfs(0) # 태평양 방문

        # 대서양 방문 여부 처리
        for i in range(m):
            visited[i][n-1][1] = 1
            queue.append((i, n-1))
        for j in range(n):
            visited[m-1][j][1] = 1
            queue.append((m-1, j))
        bfs(1) # 대서양 방문

        # 태평양과 대서양 방문한 노드 찾기
        result = []
        for i in range(m):
            for j in range(n):
                if visited[i][j][0] + visited[i][j][1] == 2:
                    result.append([i, j])

        return result