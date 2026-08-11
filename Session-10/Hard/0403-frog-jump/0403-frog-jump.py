class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            # 기록되어 있는 점프 시도
            for jump in dp[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump <= 0:
                        continue
                    
                    next_pos = stone + next_jump

                    # 건널수 있는 위치인지 확인
                    if next_pos in stones:
                        dp[next_pos].add(next_jump)
        
        return bool(dp[stones[-1]])