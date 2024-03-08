class Solution:
    def longestPalindrome(self, s: str) -> str: 
        candidates = []
        max_p = 0
        max_ps = ''
        
        if len(s) < 2:
            return s
        
        for i in range(len(s)):
            for j in [1, 2]:
                if i < len(s) - j and s[i+j] == s[i]:
                    candidates.append((i, i + j))
        
        if not candidates:
            return s[0]
        
        for c, candidate in enumerate(candidates):
            i, j = candidate
            while (i > 0) and (j < len(s) - 1):
                if s[i-1] == s[j+1]:
                    i, j = i-1, j+1
                else:
                    break
            candidates[c] = i, j

            if j - i + 1 > max_p:
                max_p = j - i + 1
                max_ps = s[i:j+1]

        return max_ps

                
    def longestPalindrom_2(self, s: str) -> str:
        if len(s) < 2:
            return s
        ps = s[0]

        for i in range(len(s)):
            for di in [1, 2]:
                if i < len(s) - di and s[i+di] == s[i]:
                    j = i + di

                    while (i > 0) and (j < len(s) - 1):
                        if s[i-1] == s[j+1]:
                            i, j = i-1, j+1
                        else:
                            break

                    if j - i + 1 > len(ps):
                        ps = s[i:j+1]
        
        return ps
                




# _test = Solution().longestPalindrome
# i = 'aaa'
# print(_test(i))