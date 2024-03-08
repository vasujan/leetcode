class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT =  2**31 - 1
        x_ = x
        x = abs(x)
        sign = -1 if x_ < 0 else 1
        y = 0
        max_y = MAX_INT + ((1 - sign) // 2)
        i = 0
        
        while x:
            xd = x % 10
            x //= 10
            y *= 10
            y += xd
            i += 1

            if i > 9 and y > max_y:
                return 0
            
        return sign * y



_test = Solution().reverse
x = -8463847412
_test(x)