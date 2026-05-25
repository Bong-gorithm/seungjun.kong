class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        if not nums:
            return result

        start = nums[0]

        for i in range(len(nums)):
            is_last = i== len(nums) - 1
            is_not_continuous = not is_last and nums[i] + 1 != nums[i + 1]
            
            if is_last or is_not_continuous:
                num_range = f"{start}" if start == nums[i] else f"{start}->{nums[i]}"
                result.append(num_range)
                
                if not is_last:
                    start = nums[i + 1] # 초기화

        return result