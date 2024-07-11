class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                start = stack.pop()
                end = i
                # Reverse the substring between the matching parentheses
                s[start:end + 1] = s[start:end + 1][::-1]
        
        # Remove all parentheses from the string
        return ''.join([char for char in s if char not in '()'])
