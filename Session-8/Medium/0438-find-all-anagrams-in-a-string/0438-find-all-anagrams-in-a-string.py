class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        p_counts = [0] * 26
        window = [0] * 26

        for ch in p:
            idx = ord(ch) - ord('a')
            p_counts[idx] += 1

        for i in range(len(s)):
            # 오른쪽 한칸씩 밀기
            idx = ord(s[i]) - ord('a')
            window[idx] += 1

            # 왼쪽 문자 제거
            if i >= len(p):
                window[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if window == p_counts:
                answer.append(i - len(p) + 1) # 첫단어의 인덱스
        
        return answer