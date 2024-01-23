class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a, b = i + 1, len(nums) - 1

            while a < b:
                _sum = nums[a] + nums[b] + nums[i]
                if _sum < 0:
                    a += 1
                elif _sum > 0:
                    b -= 1
                else:
                    res.append(nums[i], nums[a], nums[b])
                    a += 1
                    while nums[a] == nums[a-1] and a < b:
                        a += 1
        return res

    def threeSum_0(self, nums: list[int]) -> list[list[int]]:
        bucket = {}

        for i in nums:
            bucket[i] += 1

        res = []
        
        bucket_k = bucket.keys()

        for i, bi in enumerate(bucket_k):
            for j, bj in enumerate(bucket_k[i:]):
                if j == i and bi < 2:
                    continue
                part = bi + bj
                
                if bucket.get(-part, 0) == 0:
                    continue
                if (part != bi or part != bj) \
                or (part == bi and bucket[bi] > 1) \
                or (part == bj and bucket[bj] > 1):
                    res.append([bi, bj, part])
                    
        return res
