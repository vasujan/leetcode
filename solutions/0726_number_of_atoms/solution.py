class Solution:
    def countOfAtoms(self, formula: str) -> str:
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '0123456789'
        n = len(formula)
        stack = [dict()]

        def multiply(count, x):
            for k in count:
                count[k] *= x

        def merge(count, count_other):
            for k, v in count_other.items():
                count[k] = count.get(k, 0) + v
        
        current = ''
        i = 0
        while i < n:
            number = ''
            c = formula[i]
            
            if c in upper_case:
                current = c
                i += 1
                if i < n and formula[i] in lower_case:
                    current += formula[i]
                    i += 1
                stack[-1][current] = stack[-1].get(current, 0) + 1
                    
            elif c in numbers:
                number = c
                i += 1
                while i < n and formula[i] in numbers:
                    number += formula[i]
                    i += 1
                stack[-1][current] += int(number) - 1
                
            elif c == '(':
                stack.append(dict())
                i += 1

            elif c == ')':
                i += 1
                stack_last = stack.pop()
                while i < n and formula[i] in numbers:
                    number += formula[i]
                    i += 1
                if number:
                    multiply(stack_last, int(number))
                merge(stack[-1], stack_last)

        counts = stack[0]
        result = [f"{k}{v if v > 1 else ''}" for (k, v) in sorted(counts.items(), key=lambda x: x[0])]
        return "".join(result)

