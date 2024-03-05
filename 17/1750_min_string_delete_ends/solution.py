class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                l = left + 1
                r = right - 1
                while l <= r and s[l-1] == s[l]:
                    l += 1
                while r > l and s[r+1] == s[r]:
                    r -= 1
                left = l 
                right = r 
            else:
                break

        return max(right - left + 1, 0)
            