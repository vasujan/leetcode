class Solution:        
    def isMatch(self, s: str, p: str) -> bool:
        string = s
        pattern = p

        count_asterisk = sum(1 for p in pattern if p == '*')
        min_chars = len(pattern) - count_asterisk * 2

        if len(string) < min_chars:
            return False
        
        if count_asterisk:
            i, c = self.matchRepeating(string, self.patternTerms(pattern))
            return i > -1 and c >= min_chars
        else:
            i = self.matchStatic(string, pattern)
            return i > -1


    def matchStatic(self, string: str, pattern: str) -> int:
        ns = len(string)
        np = len(pattern)

        if np > ns:
            return -1
        elif np == ns and string == pattern: 
            return 0  # early exit in case exact match found
        
        min_checks = ns - np + 1

        for i in range(min_checks):
            for j in range(np):
                if string[i+j] == pattern[j] or pattern[j] == '.':
                    continue
                else:
                    break
            else:
                return i
        else:
            return -1
        
    def firstRepeatingSubstring(self, string: str, char: str) -> tuple[int, int]:
        if len(char) != 1:
            raise ValueError("Char should be one.")
        
        found = False
        i, found = 0, 0

        for ci, c in enumerate(string):
            if found and c != char:
                break
            if c == char:
                if not found:
                    i = ci
                found += 1
        
        return i, found
    
    def patternTerms(self, pattern: str) -> list[str]:
        groups = []
        i = 0
        for pi in range(1, len(pattern)):
            if pattern[pi] == '*':
                if pi - i > 1:
                    groups.append(pattern[i:pi-1])
                groups.append(pattern[pi-1:pi+1])
                i = pi + 1
        else:
            if i < len(pattern) - 1:
                groups.append(pattern[i:])
        
        return groups
            
            
    def matchRepeating(self, string: str, pattern_groups: list[str]) -> bool:
    
        n = len(string)
        
        pattern_groups = [{
                "pattern": p,
                "repeating": len(p) == 2 and p[1] == '*'
        
        } for p in pattern_groups]

        for p in pattern_groups:
            p["min_len"] = 0 if p["repeating"] else len(p)
            p["max_len"] = None if p["repeating"] else len(p)
            p["char"] = p["pattern"][0] if p["repeating"] else None
            p["start"] = None
            p["end"] = None
            p["len"] = None

        min_len = 0
        for p in pattern_groups[::-1]:
            p["right_pad"] = min_len
            min_len += p["min_len"]
        
        left_pad = 0
        for p in pattern_groups:
            p["left_pad"] = left_pad
            if p["char"]:
                p["max_len"] = n - p["left_pad"] - p["right_pad"]
            else:
                p["max_len"] = p["min_len"]
            left_pad += p["min_len"]
        

s = Solution().matchRepeating('abcdefgh', 'ab.*gh')
print(s)