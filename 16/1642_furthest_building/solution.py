from typing import List
import heapq

def add_pop(arr: list, item: int, capacity: int):

    for i in range(len(arr)):
        if item > arr[i]:
            arr.insert(i, item)
            break
    else:
        arr.append(item)
    
    if len(arr) > capacity:
        return arr.pop()

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        max_heap = list()
        for i in range(1, len(heights)):
            gap = heights[i] - heights[i-1]
            if gap <= 0:
                continue

            if ladders > 0:
                heapq.heappush(max_heap, gap)
                if len(max_heap) > ladders:
                    bricks -= heapq.heappop(max_heap)
            else:
                bricks -= gap

            if bricks < 0:
                return i - 1

        else:
            return len(heights) - 1

s = Solution()
heights = [14,3,19,3]
bricks = 17
ladders = 0
r = s.furthestBuilding(heights, bricks, ladders)
print(r)            
            
        
