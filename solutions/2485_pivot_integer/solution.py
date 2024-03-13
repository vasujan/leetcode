class Solution:
    def pivotInteger(self, n: int) -> int:
        prev_sum = 0
        N = (n + 1) * n // 2
        for i in range(1, n + 1):
            if prev_sum + i == N - prev_sum:
                return i
            prev_sum += i
        else:
            return -1