class Solution:
    def numSteps(self, s: str) -> int:
        """
        Reduce a binary string to "1" by:
        1. Dividing by 2 if even (last bit is 0) - 1 step
        2. Adding 1 then dividing by 2 if odd (last bit is 1) - 2 steps

        Optimized approach: Process from right to left with carry tracking.
        - bit=0, no carry: divide by 2 (1 step)
        - bit=1, no carry: add 1 (creates carry, becomes 0) then divide (2 steps)
        - bit=1, carry: carry + bit = 2, becomes 0 with carry (1 step)
        - bit=0, carry: carry + bit = 1, then divide (1 step)

        Time: O(n) where n is length of string
        Space: O(1) - no string modifications
        """
        steps = 0
        carry = 0

        # Process from right to left, stop before the leading 1
        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit % 2 == 1:  # Odd
                steps += 2
                carry = 1
            else:  # Even
                steps += 1

        # Handle the leading bit with any remaining carry
        steps += carry

        return steps
