from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        Given an integer n, return 1 - n in lexicographical order.

        The function takes a single integer argument, n, and returns a list of integers containing the numbers 1 through n in lexicographical order.

        :param n: An integer
        :return: A list of integers
        """
        result = []
        current_number = 1
        for _ in range(n):
            result.append(current_number)
            if current_number * 10 <= n:
                current_number *= 10
            elif current_number == n or current_number % 10 == 9:
                current_number //= 10
                while current_number % 10 == 9:
                    current_number //= 10
                current_number += 1
            else:
                current_number += 1
        return result
