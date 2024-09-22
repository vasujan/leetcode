import sys
sys.path.append('.')
from scripts.leetcode_test import LeetcodeTest
from solution import Solution
from pathlib import Path
import unittest

class TestSolution(unittest.TestCase):
    pass

if __name__ == '__main__':
    lct = LeetcodeTest(Path(__file__).parent)
    solution = Solution.findKthNumber
    test_cases = lct.generate_test_cases(lct.test_file_path("test_cases.txt"))
    lct.add_test_cases(TestSolution, solution, test_cases)
    unittest.main()
