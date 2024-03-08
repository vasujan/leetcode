from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(candies)):
            if ratings[i] > ratings[i - 1]:
                candies[i] += candies[i - 1]
            
        for j in reversed(range(0, len(candies) - 1)):
            if ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j + 1] + 1

        return sum(candies)