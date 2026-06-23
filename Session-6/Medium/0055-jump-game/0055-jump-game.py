class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)
        result = 0

        for i in range(size):
            if i > result:
                return False

            result = max(result, i + nums[i])

        return True