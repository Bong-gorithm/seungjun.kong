class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        idx = [0] * len(primes)

        for i in range(1, n):
            candidates = []

            for j in range(len(primes)):
                candidates.append(primes[j] * dp[idx[j]])
            
            next_num = min(candidates)
            dp[i] = next_num

            for j in range(len(primes)):
                if candidates[j] == next_num:
                    idx[j] += 1
        
        return dp[n - 1]