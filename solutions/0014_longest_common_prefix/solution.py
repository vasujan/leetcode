class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        
        for s in strs[1:]:
            i = 0
            while i < len(pref) and i < len(s):
                if pref[i] != s[i]:
                    break
                i += 1
            pref = pref[:i]
        
        return pref



    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]


        for s in strs:
            if len(s) < len(prefix):
                prefix = prefix[:len(s)]
            pn = len(prefix)
            i = 0
            while i < pn and prefix[i] == s[i]:
                i += 1

            prefix = prefix[:i]
        return prefix

s = ["cir","car"]
Solution().longestCommonPrefix(s)