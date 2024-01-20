from typing import List
class MStack:

    def __init__(self):
        self.arr: list[list[int]] = []
        self.sum = 0

    def top(self):
        if not self.arr:
            return None
        else:
            return self.arr[-1]
    
    def push(self, n):

        t = self.top()
        if not t or (t and n > t[0]):
            self.arr.append([n, 1])
            self.sum += n
            return
        elif n == t[0]:
            t[1] += 1
            self.sum += n
        else:
            nn = 1
            while self.top() and n < self.top()[0]:
                p = self.arr.pop()
                self.sum -= p[0] * p[1]
                nn += p[1]
            self.arr.append([n, nn])
            self.sum += (n * nn)


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res: int = 0

        m_stack = MStack()
        for a in arr:
            m_stack.push(a)
            res += m_stack.sum
            
