class Solution:
    def maxArea_dp(self, height: list[int]) -> int:
        """

        (i)
        n-1     
        n-2                         .
        ~                       ~   ~
        ~                   ~   ~   ~
        2               .   .   .   .
        1           .   .   .   .   .
        0       .   .   .   .   .   .
            0   1   2   -   -   n-2 n-1 (j)
        

        """
        n = len(height)

        def area(i, j): 
            if j <= i:
                return 0
            
            min_height = min(height[i], height[j])
            cur_area = min_height * (j - i)

            if j > i:
                cur_area = max(cur_area, area(i, j-1))
            
            return max(cur_area, area(i+1, j))
            
        
        return area(0, n-1)

    def maxArea(self, height: list[int]) -> int:
        res = 0
        i, j = 0, len(height) - 1

        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(res, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
        return res

height = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]

    
print(Solution().maxArea(height))

