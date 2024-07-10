class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        current = 0

        while len(circle) > 1:
            
            eliminate = (current + k - 1) % len(circle)
            # print(circle, current, eliminate, circle[eliminate])
            circle.pop(eliminate)
            current = (eliminate) % len(circle)

        return circle[0]
