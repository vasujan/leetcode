class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Given a string s, you can perform a palindrome transformation on any prefix of s, 
        which means you can add characters to the front of the prefix to make it a palindrome.

        Return the shortest palindrome you can create from s by performing the above transformation.

        :param s: input string
        :return: the shortest palindrome
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s