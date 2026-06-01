class Solution:
    def longestPalindrome(self, s: str) -> int:
        check_set = set()

        count = 0
        for c in s:
            if c in check_set:  # 중복인 경우
                check_set.remove(c)
                count += 2
            else:
                check_set.add(c)
        
        if check_set:
            count += 1
        
        return count        