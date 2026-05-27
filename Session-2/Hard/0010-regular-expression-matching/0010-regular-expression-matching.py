class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

        # [0, 0] [0번째 글자, 0번째 패턴] "" == ""
        dp[0][0] = True

        # 빈 문자열과 매칭 가능한 패턴 초기화 a*, a*b*, .*
        for i in range(2, p_len + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 2]
        
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                # 일반 문자 or . 매칭
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                # * 매칭
                elif p[j - 1] == "*":
                    # 앞 문자 + * 0 번 사용
                    dp[i][j] = dp[i][j - 2]

                    # 앞 문자 + * 1번 이상 사용
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        return dp[s_len][p_len]