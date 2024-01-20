

class Solution: 
    def isMatch(self, s: str, p: str) -> bool:
        string = s
        pattern = p

        count_asterisk = sum(1 for p in pattern if p == '*')
        min_chars = len(pattern) - count_asterisk * 2
        
        if len(string) < min_chars:
            return False
        
        if count_asterisk:
            return self.matchGroup(string, self.patternTerms(pattern))
        else:
            return self.matchStatic(string, pattern)
             

    def matchGroup(self, string: str, pattern_group: list[str]) -> bool:
        ns = len(string)
        np = len(pattern_group)

        patterns = pattern_group
        expand = [len(p) == 2 and p[1] == '*' for p in patterns]
        required_len = [0 if e else len(p) for p, e in zip(patterns, expand)]

        offset = 0
        len_offset = [0 for _ in patterns]
        for pi in range(np - 1, -1, -1):
            len_offset[pi] = offset
            offset -= required_len[pi]
        
        buffer = []

        si = 0
        pi = 0
        while si < ns or pi < np:
            if pi < np and expand[pi]:
                count = self.countRepeating(string[si:], patterns[pi][0])
                limit = ns + len_offset[pi] - si
                assert limit >= 0
                p_len = min(count, limit)
                if p_len:
                    buffer.append([pi, si, p_len])
                si += p_len
                pi += 1
                continue
            elif pi < np:
                p_len = len(patterns[pi])
                match = self.matchStatic(string[si:si+p_len], patterns[pi])
                if match:
                    si += p_len
                    pi += 1
                    continue
            if pi == np and si < ns:
                return False
            if not buffer:
                return False
            b = buffer[-1]
            if b[2]:
                si = b[1] + b[2]
                buffer[-1][2] -= 1
            else:
                si = b[1]
                buffer.pop()
            pi = b[0] + 1
        else:
            return True
                
                

    def countRepeating(self, string: str, char: str) -> int:
        if len(char) > 1:
            raise ValueError("Character should be singular")
        if char == '.':
            return len(string)
        
        c = 0
        for s in string:
            if s == char:
                c += 1
            else:
                break
        
        return c

    def matchStatic(self, string: str, pattern: str) -> bool:
        ns = len(string)
        np = len(pattern)

        if np != ns:
            return False
        
        for i in range(np):
            if string[i] != pattern[i] and pattern[i] != '.':
                return False
        else:
            return True
        
    def patternTerms(self, pattern: str) -> list[str]:
        groups = []
        i = 0
        for pi in range(1, len(pattern)):
            if pattern[pi] == '*':
                if pi - i > 1:
                    groups.append(pattern[i:pi-1])
                p = pattern[pi-1:pi+1]
                if len(groups) == 0 or p != groups[-1]:
                    groups.append(p)
                i = pi + 1
        else:
            if i < len(pattern):
                groups.append(pattern[i:])
        
        return groups

# print(Solution().matchGroup('abccdef', ['abc', 'cdef']))
# print(Solution().patternTerms('c*a*b'))
# print(Solution().patternTerms("mis*is*p*.")) 
s = "bbcbbcbcbbcaabcacb"
p = "a*.*ac*a*a*.a..*.*"
    
print(Solution().isMatch(s, p))