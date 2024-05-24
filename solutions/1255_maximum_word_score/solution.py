import unittest
from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        letters_count = Counter(letters)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alphabet_score = {k: v for k, v in zip(alphabets, score)}

        self.max_score = 0
        
        def word_score(word: str):
            return sum(alphabet_score[l] for l in word)
    
        def can_form(word: str, letters_count: Counter) -> bool:
            word_count = Counter(word)
            for letter, count in word_count.items():
                if letters_count[letter] < count:
                    return False
            return True
 
        def dfs(index: int, current_score: int, letters_count: Counter):
            if index == len(words):
                self.max_score = max(self.max_score, current_score)
                return

            dfs(index + 1, current_score, letters_count)

            word = words[index]
            if can_form(word, letters_count):
                for letter in word:
                    letters_count[letter] -= 1

                dfs(index + 1, current_score + word_score(word), letters_count)

                for letter in word:
                    letters_count[letter] += 1
        

        dfs(0, 0, letters_count)
        return self.max_score
    

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        words = ["dog", "cat", "dad", "good"]
        letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 23)

    def test_case_2(self):
        words = ["xxxz", "ax", "bx", "cx"]
        letters = ["z", "a", "b", "c", "x", "x", "x"]
        score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 27)

    def test_case_3(self):
        words = ["leetcode"]
        letters = ["l", "e", "t", "c", "o", "d"]
        score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 0)

    def test_case_4(self):
        words = ["a", "aa", "aaa", "aaaa"]
        letters = ["a", "a", "a", "a"]
        score = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 4)

    def test_case_5(self):
        words = ["dog", "cat", "dad", "good"]
        letters = ["a", "a", "c", "d", "d", "g", "o", "o"]
        score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 12)

    def test_case_6(self):
        words = ["dog", "cat", "dad", "good"]
        letters = ["d", "a", "d", "g", "o"]
        score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 11)

    def test_case_7(self):
        words = ["abc", "def", "ghi"]
        letters = ["a", "b", "c", "d", "e", "f"]
        score = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 6)

    def test_case_8(self):
        words = ["a", "b", "c", "d", "e"]
        letters = ["a", "b", "c", "d", "e"]
        score = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 5)

    def test_case_9(self):
        words = ["apple", "banana", "cherry"]
        letters = ["a", "p", "l", "e", "b", "n", "c", "h", "r", "y"]
        score = [1,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 0)

    def test_case_10(self):
        words = ["xyz", "xyz", "xyz"]
        letters = ["x", "y", "z", "x", "y", "z"]
        score = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.maxScoreWords(words, letters, score), 6)

if __name__ == '__main__':
    unittest.main()
