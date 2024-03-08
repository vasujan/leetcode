class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = reversed(s)

        res = 0
        for i in s:
            if res > 0 and i == ' ':
                break
            if i != ' ':
                res += 1
        
        return res