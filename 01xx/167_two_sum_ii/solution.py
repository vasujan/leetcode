class Solution:

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Two pointer in opposite direction."""
        n = len(numbers)
        i, j = 0, n-1

        while i < j:
            sum_ = numbers[i] + numbers[j]
            if sum_ < target:
                i += 1
            elif sum_ > target:
                j -= 1
            else:
                return [i+1, j+1] # solution requires index starting from 1



    def twoSum_naive(self, numbers: list[int], target: int) -> list[int]:
        """Naive two pointer in same direction."""

        id_1, id_2 = 0, 1

        while id_1 < len(numbers) - 1: # for id_2 > id_1 and avoid index overflow

            # early exit
            # id_1+=1 when target - num[id_1] < num[id_1] as there is number smaller ahead
            if (target - numbers[id_1]) < numbers[id_1] \
                or id_2 == len(numbers):
                
                id_1 += 1
                id_2 = id_1 + 1

            if numbers[id_1] + numbers[id_2] == target:
                break
            elif (numbers[id_1] == numbers[id_2]):
                id_1 += 1
                id_2 = id_1 + 1

            id_2 += 1

        return [id_1 + 1, id_2 + 1] # output indices start from 1

