class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # 왼쪽 아이 비교
        for i in range(0, n - 1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
        
        # 오른쪽 아이 비교
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)

        return sum(candies)