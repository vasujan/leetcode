class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        return '1' * (count_one - 1) + '0' * (len(s) - count_one) + '1'
