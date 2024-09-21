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
    test_solution = TestSolution
    solution = Solution
    test_cases = lct.generate_test_cases(lct.test_file_path("test_cases.txt"))
    lct.add_test_cases(test_solution, solution, test_cases)
    unittest.main()
