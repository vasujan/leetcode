class MountainArray:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.get_count = 100

    def get(self, index: int) -> int:
        if self.get_count > 0:
            self.get_count -= 1
            return self.arr[index]
        else:
            raise ValueError(self.get_count, "API Expired")
        

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        memo: dict[int, int] = dict()
        length = mountain_arr.length()

        def get(i: int) -> int:
            return memo.setdefault(i, mountain_arr.get(i))

        def find_m(l: int, r: int) -> int:
            return (l + r) // 2

        def get_mid(m):
            mid = (get(m-1), get(m), get(m+1))
            return mid
        

        # Find peak
        l, r = 0, length - 1
        while l <= r:
            m = find_m(l, r)
            mid = get_mid(m)

            if mid[0] < mid[1] < mid[2]:
                l = m + 1
            elif mid[0] > mid[1] > mid[2]:
                r = m - 1
            else:
                break
        peak = m

        
        # m = find_m(l, r)
        # mid = get_mid(m)
        # while mid[1] < mid[0] or mid[1] < mid[2]:
        #     if mid[1] < mid[0]:
        #         l, r = l, m
        #     elif mid[1] < mid[2]:
        #         l, r = m, r
        #     else:
        #         break
        #     m = find_m(l, r)
        #     mid = get_mid(m)
        
        # peak = m

        # def bin_search(l, r, val, order=1):
        #     val = order * val
        #     while l <= r:
        #         m = find_m(l, r)
        #         mv = get(m) * order

        #         if mv < val:
        #             l, r = m + 1, r
        #         elif mv > val:
        #             l, r = l + 1, m
        #         else:
        #             return m
        #     else:
        #         return -1

        # Search left
            
        l, r = 0, peak
        while l <= r:
            m = find_m(l, r)
            val = get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # Search right
                    
        l, r = peak, length - 1
        while l <= r:
            m = find_m(l, r)
            val = get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
            
        return -1


    def test(self, tests:list):
        for arg in tests:
            t, m = arg[0], MountainArray(arg[1])
            exp = arg[2]
            res = self.findInMountainArray(t, m)
            print(arg)
            print(exp==res, exp, res)

s = Solution()
s.test([
    (3, [1, 2, 3, 4, 5, 3, 1], 2),
    (3, [0, 1, 2, 4, 2, 1], -1),
    (1, [1, 5, 2], 0),
    (2, [1, 2, 3, 4, 5, 3, 1], 1),
    (2, [1, 5, 2], 2),
    (0, [1, 5, 2], -1),
    (1, [1,2,5,1], 0),
    (0, [3,5,3,2,0], 4),
])