from functools import reduce

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def combine_letters(given: list[str], digit: str):
            chars = mapping[digit]
            if not given:
                return list(chars)
            return [g + c for g in given for c in chars]

        digits = list(digits)
        return reduce(combine_letters, digits, [])
        