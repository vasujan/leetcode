class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        si = 0
        ti = 0

        while ti < len(t) and si < len(s):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        
        return si == len(s)
            