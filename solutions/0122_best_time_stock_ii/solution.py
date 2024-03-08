from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices) - 1:
            change = prices[i + 1] - prices[i]
            if change > 0:
                profit += change
            i += 1
        
        return profit