from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_buy = 10**4 + 1
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)
        
        return max_profit