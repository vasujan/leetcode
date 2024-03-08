class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        ni = hi = 0
        while (hi + ni) < len(haystack) and ni < len(needle):
            if haystack[hi + ni] != needle[ni]:
                hi += 1
                ni = 0
            else:
                ni += 1
            
        return hi if ni == len(needle) else -1