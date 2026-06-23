class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height) 
        left_max = [0 for _ in range(size)]
        right_max = [0 for _ in range(size)]

        for i in range(1, size):
            left_max[i] = max(left_max[i-1], height[i-1])
            right_max[-i-1] = max(right_max[-i], height[-i])

        output = 0
        for i in range(size):
            water = min(left_max[i], right_max[i]) - height[i]

            if water > 0:
                output += water
                
        return output