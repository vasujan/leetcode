class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        letters += str.upper(letters)
        letters += '0123456789'

        clean = ''
        for c in s:
            if c in letters: clean += str.lower(c)
        
        i, j = 0, len(clean) - 1

        while i < j:
            if clean[i] == clean[j]:
                i += 1
                j -= 1
            else:
                return False
        else:
            return True