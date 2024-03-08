class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            1: 'I',
            5: 'V', 4: 'IV',
            10: 'X', 9: 'IX',
            50: 'L', 40: 'XL',
            100: 'C', 90: 'XC',
            500: 'D', 400: 'CD',
            1000: 'M', 900: 'CM'
        }

        levels = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        res = ''
        for level in levels:
            while level <= num:
                res += map[level]
                num -= level
        
        return res


    def intToRoman(self, num: int) -> str:
        res = ''
        num_ = num
        def romans(rem, d_1, d_5, d_10):
            if rem < 1:
                return ''
            elif rem < 4:
                return d_1 * rem
            elif rem == 4:
                return d_1 + d_5
            elif rem < 9:
                return d_5 + d_1 * (rem % 5)
            elif rem == 9:
                return d_1 + d_10


        pos_1 = romans(num % 10, 'I', 'V', 'X')
        num //= 10
        pos_2 = romans(num % 10, 'X', 'L', 'C')
        num //= 10
        pos_3 = romans(num % 10, 'C', 'D', 'M')
        num //= 10
        pos_4 = romans(num, 'M', '', '')

        return pos_4 + pos_3 + pos_2 + pos_1
    
# for i in range(3990, 4000):
#     print(i, Solution().intToRoman(i))

print(Solution().intToRoman(3999))
