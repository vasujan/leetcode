class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            exchanges = numBottles // numExchange
            numBottles -= exchanges * (numExchange - 1)
            result += exchanges
        
        return result
