class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        res: int = 0
        stack = []
        _sum = 0

        def push(n):
            if not stack or stack[-1][0] < n:
                stack.append([n, 1])
                change = n
            elif stack[-1][0] == n:
                stack[-1][1] += 1
                change = n
            else:
                change = 0
                nn = 1
                while stack and n < stack[-1][0]:
                    p = stack.pop()
                    change -= p[0] * p[1]
                    nn += p[1]
                stack.append([n, nn])
                change += n * nn
            return change
            
        for a in arr:
            _sum += push(a)
            res += _sum
            
        res %= 10**9 + 7
        return res