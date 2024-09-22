class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int) -> int:
            """ Counts how many numbers exist between prefix and next prefix in lexicographical order. """
            current = prefix
            next_prefix = prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        current_number = 1
        k -= 1  # The first number is 1, so we decrement k to find the k-th number.

        while k > 0:
            count = count_prefix(current_number, n)
            if count <= k:
                # If the current prefix range doesn't contain the k-th number, move to the next prefix.
                k -= count
                current_number += 1
            else:
                # If the current prefix range contains the k-th number, go deeper into the prefix.
                k -= 1
                current_number *= 10

        return current_number
