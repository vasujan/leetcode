class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        level = 1000
        res = 0
        for char in s:
            val = map[char]
            if val <= level:
                res += val
                level = val
            else:
                res += val - 2 * level
                level = val
            
        return res


    def romanToInt(self, s: str) -> int:
        res = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] == 'I':
                if res < 4:
                    res += 1
                else:
                    res -= 1
            elif s[i] == 'V':
                res += 5 
            elif s[i] == 'X':
                if res < 40:   
                    res += 10
                else:
                    res -= 10
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'C':
                if res < 400:
                    res += 100
                else:
                    res -= 100
            elif s[i] == 'D':
                res += 500
            elif s[i] == 'M':
                res += 1000

            if res > 3999:
                raise OverflowError()
            
            i -= 1
        
        return res
    
print(Solution().romanToInt('MMMCMXCIX'))
            
