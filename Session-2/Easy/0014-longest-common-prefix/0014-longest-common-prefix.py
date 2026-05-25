class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_length = len(strs[0])

        for s in strs:
            min_length = len(s) if len(s) < min_length else min_length
        
        for i in range(min_length):
            common = strs[0][i]

            for s in strs:
                if s[i] != common:
                    return strs[0][:i]
            
        return strs[0][:min_length]