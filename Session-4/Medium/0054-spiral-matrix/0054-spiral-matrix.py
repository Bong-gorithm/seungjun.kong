class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        m, n = len(matrix), len(matrix[0]) 
        
        x, y = 0, 0
        direction = 0
        
        output = []
        total = m * n
        while len(output) < total:
            output.append(matrix[x][y])
            matrix[x][y] = 101

            dx, dy = order[direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] <= 100: # 계속 한방향으로 이동가능한지
                x, y = nx, ny
            else: # 방향 전환
                direction = (direction + 1) % 4
                dx, dy = order[direction]
                x, y = x + dx, y + dy

        return output