class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        opening = ["{", "[", "("]

        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            elif stack and stack[-1] == closing[c]:
                stack.pop()
            else:
                return False
        else:
            return not stack