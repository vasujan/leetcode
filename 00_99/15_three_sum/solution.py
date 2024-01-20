class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
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
