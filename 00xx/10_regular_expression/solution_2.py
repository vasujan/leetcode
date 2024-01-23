from typing import Self

class PatternGroup:
    def __init__(self, patterns: list["Pattern"]):
        self.patterns = patterns
        
    

class Pattern:
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
        self.len = len(self.pattern)
        self.is_expanding = '*' in self.pattern
        if (self.is_expanding and self.len < 2) or self.pattern[0] == '*':
            raise ValueError(f"Wrong pattern provided: {self.pattern}")

        if self.is_expanding and self.len > 2:
            self.is_atomic = False
        else:
            self.is_atomic = True

    def __repr__(self):
        return f'Pattern("{self.pattern}")'

    def terms(self) -> PatternGroup:
        groups = []
        i = 0
        pattern = self.pattern
        for pi in range(1, self.len):
            if pattern[pi] == '*':
                if pi - i > 1:
                    groups.append(pattern[i: pi-1])
                groups.append(pattern[pi-i: pi+1])
                i = pi + 1
        else:
            if i < self.len - 1:
                groups.append(pattern[i:])
        
        return PatternGroup([self.__class__(p) for p in groups])

    def match_static(self, string: str) -> int:
        ns = len(string)
        np = self.len
        if np > ns:
            return -1
        elif np == ns and string == self.pattern:
            return 0
        
        min_checks = ns - np + 1

        for i in range(min_checks):
            for j in range(np):
                if string[i+j] != self.pattern[j] \
                    or self.pattern[j] != '.':
                    break
            else:
                return i
        else:
            return -1
        
        

    

class Solution:
    pass



s = Pattern("abc.*bc")
print(s.make_groups())