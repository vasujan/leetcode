from dataclasses import make_dataclass

ElementFrequency = make_dataclass("ElementFrequency", [("element", int), ("frequency", int)])

class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        result: int = 0
        stack = []
        current_sum = 0

        def push(element):
            nonlocal current_sum
            nonlocal stack

            # If stack is empty or current element is greater, add a new element to the stack
            if not stack or stack[-1].element < element:
                stack.append(ElementFrequency(element, 1))
                change = element
            # If current element is equal to the top of the stack, update the frequency
            elif stack[-1].element == element:
                stack[-1].frequency += 1
                change = element
            # If current element is smaller, pop elements from stack and update result
            else:
                change = 0
                frequency = 1
                while stack and element < stack[-1].element:
                    popped = stack.pop()
                    change -= popped.element * popped.frequency
                    frequency += popped.frequency
                stack.append(ElementFrequency(element, frequency))
                change += element * frequency

            return change

        for current_element in arr:
            current_sum += push(current_element)
            result += current_sum

        result %= 10**9 + 7
        return result
