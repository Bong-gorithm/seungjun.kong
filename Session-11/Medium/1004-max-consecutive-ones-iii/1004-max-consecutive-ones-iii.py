class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        zero_cnt = k
        max_length = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero_cnt -= 1

            # 1 뒤집은 경우가 초과한경우, 다시 회수할때까지 반복
            while zero_cnt < 0:
                if nums[start] == 0:
                    zero_cnt += 1
                start += 1
            
            # 한칸 이동
            max_length = max(max_length, i - start + 1)
        
        return max_length
