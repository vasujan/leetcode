class Solution:
    def lengthOfLongestSubstring_list(self, s: str) -> int:
        streak = []
        longest = 0

        for c in s:
            if c in streak:
                longest = max(len(streak), longest)
                c_index = streak.index(c)
                streak = streak[c_index+1:]
            streak.append(c)
        
        return max(len(streak), longest)

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = result = 0

        for i, c in enumerate(s):
            if seen.get(c, -1) >= start:
                start = seen[c] + 1
            result = max(result, i - start + 1)
            seen[c] = i
        
        return result