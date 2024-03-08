class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        a, b = 0, 0

        while b < len(s):
            if a == b and s[a] == ' ':
                a += 1
                b += 1
            elif s[b] != ' ': 
                b += 1
            else: 
                res = s[a: b + 1] + res
                a = b 
        
        if a < b:
            res = s[a:] + ' ' + res
        
        return res[:-1]
            