class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        m, n = len(image), len(image[0])
        base = image[sr][sc]

        if base == color:
            return image

        def dfs(x, y):
            image[x][y] = color
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < m and 0 <= ny < n:
                    if base == image[nx][ny]:
                        dfs(nx, ny)
        
        dfs(sr, sc)

        return image