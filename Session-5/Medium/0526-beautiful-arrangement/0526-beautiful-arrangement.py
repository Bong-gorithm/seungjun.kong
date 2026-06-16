class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        output = 0

        def dfs(pos):
            nonlocal output
            if pos == n + 1:
                output += 1
                return 
            
            for i in range(1, n+1):
                if visited[i]:
                    continue
                
                if pos % i == 0 or i % pos == 0:
                    visited[i] = True
                    dfs(pos + 1)
                    visited[i] = False
        dfs(1)
        return output