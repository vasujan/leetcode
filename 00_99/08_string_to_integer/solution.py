class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -(2**31)
        NUMBERS = '0123456789'
        SIGNS = '-+'
        IGNORE = ' '

        str = ''

        for c in s:
            if not str and c in SIGNS:
                str += c
            elif c in NUMBERS:
                str += c
            elif not str and c in IGNORE:
                continue
            else:
                break

        if not str or str in SIGNS:
            return 0
        output = int(str)
        if output < MIN:
            return MIN
        elif output > MAX:
            return MAX
        else:
            return output
    
Solution().myAtoi("+0  123")