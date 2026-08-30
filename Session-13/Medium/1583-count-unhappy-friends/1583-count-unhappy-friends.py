class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhappy = set()
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for order, friend in enumerate(preferences[i]):
                rank[i][friend] = order # 숫자가 작을수록 더 선호도 높음

        for x in range(n):
            y = partner[x]

            for u in preferences[x]:
                if rank[x][u] >= rank[x][y]:
                    break # x가 y 보다 선호하는 사람이 없는 경우
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy.add(x)
                    break

        return len(unhappy)