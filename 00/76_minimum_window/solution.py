class Solution:

    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        chars = dict()
        for ti in t:
            if ti in chars:
                chars[ti] += 1
            else:
                chars[ti] = 1

        if len(s) < len(t):
            return min_window

        for i, si in enumerate(s):
            if si not in t:
                continue
            
            t_chars = chars.copy()

            j = i
            while j < len(s):
                if s[j] in t_chars:
                    t_chars[s[j]] -= 1
            
                if sum(t_chars.values()) == 0:
                    cur_window = s[i:j+1]
                    if min_window != "" or len(cur_window) < len(min_window):
                        min_window = cur_window
                j += 1
        
        
        return min_window
