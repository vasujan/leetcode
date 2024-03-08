from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0

        def stringify(line, length): 
            extra_space = maxWidth - length
            if len(line) == 1:
                return line[0] + ' ' * extra_space
            
            sep = len(line) - 1
            spaces = extra_space // sep
            remainder = extra_space % sep

            for j in range(sep):
                line[j] += ' ' * spaces
                if j < remainder: line[j] += ' '
            
            return "".join(line)

        for i in range(len(words)):
            if length + len(line) + len(words[i]) > maxWidth:
                res.append(stringify(line, length))
                line, length = [], 0

            line.append(words[i])
            length += len(words[i])
            
        if line:
            last_line = " ".join(line)
            last_line += (maxWidth - len(last_line)) * ' '
            res.append(last_line)
        
        return res