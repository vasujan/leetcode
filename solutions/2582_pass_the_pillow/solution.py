
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n_t = time % ((n - 1) * 2)
        if n_t >= n:
            n_t = (n - 1) * 2 - n_t

        # 0 - 1 - 2 - 3 - 4 - 5 - 6
        # 0 - 1 - 2 - 3 - 2 - 1 - 0
        # 0 - 1 - 2 /

        return n_t + 1
