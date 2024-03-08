from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = dict()
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        need = len(t)
        res_l, res_r = -1, 10**6
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in t:
                if countT[c] > 0: need -= 1
                countT[c] -= 1

            while not need:
                if (r - l + 1) < (res_r - res_l + 1):
                    res_l, res_r = l, r
                cl = s[l]
                if cl in t:
                    countT[cl] += 1
                    if countT[cl] > 0: need += 1
                l += 1
            
        return s[res_l:res_r+1] if res_l > -1 else ""

print(Solution().minWindow("bba", "ab"))