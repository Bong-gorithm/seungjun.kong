class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_wall = [0] * n
        right_wall = [0] * n

        left_wall[0] = height[0]
        for i in range(1, n):
            left_wall[i] = max(left_wall[i-1], height[i])

        right_wall[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_wall[i] = max(right_wall[i+1], height[i])

        total = 0
        for i in range(n):
            total += min(left_wall[i], right_wall[i]) - height[i]
        
        return total
        
