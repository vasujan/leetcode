from typing import List
import unittest

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_count = [0] * n
        for road in roads:
            city_1, city_2 = road
            city_count[city_1] += 1
            city_count[city_2] += 1

        map_importance = zip(sorted(city_count), range(1, n+1))
        max_score = sum(a * b for (a, b) in map_importance)
        return max_score

class TestMaximumImportance(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        n = 5
        roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
        expected = 43
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_minimal_input(self):
        n = 2
        roads = [[0, 1]]
        expected = 3
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_maximum_input(self):
        n = 50000
        roads = [[i, (i + 1) % n] for i in range(n)]
        expected = 125000
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_large_connected_graph(self):
        n = 1000
        roads = [[i, (i + 1) % n] for i in range(n)]
        expected = 250000
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_disconnected_cities(self):
        n = 6
        roads = [[0, 1], [2, 3], [4, 5]]
        expected = 5
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_complete_graph(self):
        n = 4
        roads = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
        expected = 18
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)
    
    def test_random_large_input(self):
        import random
        n = 10000
        roads = [[random.randint(0, n-1), random.randint(0, n-1)] for _ in range(20000)]
        expected = 100000000
        self.assertEqual(self.solution.maximumImportance(n, roads), expected)

if __name__ == "__main__":
    unittest.main()