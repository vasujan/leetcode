from pathlib import Path
from collections import namedtuple
from typing import Any
class LeetcodeTest:
    TEST_FILE_NAME = "test_cases.txt"
    test_case = namedtuple("test_case", ["inputs", "outputs"])

    def __init__(self, solution_path: str):
        self.solution_path = solution_path

    def generate_test_cases(self, file_path: Path) -> list[test_case]:
        """Generate test cases from a file.

        The file is expected to contain input and output for each test case,
        separated by a blank line. Each line of input is expected to contain
        space-separated values, which will be converted to the appropriate type
        (either int or str). The output is expected to be a single line, with
        space-separated values that will be converted to str.

        Args:
            file_path (Path): The path to the file containing the test cases.

        Returns:
            A list of tuples, where each tuple contains the input and output
            for a test case.
        """
        test_cases = []
        with open(file_path, "r") as f:
            lines = f.readlines()

            for i in range(0, len(lines), 2):
                input_line = lines[i].strip()
                output_line = lines[i+1].strip()
                inputs = [self.parse_string(x) for x in input_line.split()]
                outputs = [self.parse_string(x) for x in output_line.split()]
                test_cases.append(self.test_case(inputs, outputs))
        return test_cases

    @staticmethod
    def create_test_case_func(test_case, func):
        inputs, outputs = test_case
        def test_function(self):
            result = [func(self, *inputs)]
            self.assertEqual(result, outputs)
        return test_function


    @staticmethod
    def parse_string(s: str) -> list[Any]:
    # create a function which takes in a string input which can either be 
    # string, integer, float and an array of these 
    # like "abc", 4, 2.4, ["asdf", 14, 15.9]
    # and returns a list of the same type 
    # like ["abc", 4, 2.4, ["asdf", 14, 15.9]]
        if s[0] == '[' and s[-1] == ']':
            return [LeetcodeTest.parse_string(x) for x in s[1:-1].split(',')]
        elif s[0] == '"' and s[-1] == '"':
            return s[1:-1]
        elif '.' in s:
            return float(s)
        elif s.isdigit():
            return int(s)
        else:
            raise ValueError(f"Invalid input: {s}")
    

    def test_file_path(self, file_name: str = None):
        if not file_name:
            file_name = self.TEST_FILE_NAME
        return self.solution_path / file_name

    def add_test_cases(self, test_solution, solution, test_cases):
        for i, test_case in enumerate(test_cases):
            func = self.create_test_case_func(test_case, solution)
            test_name = f"test_case_{i}"
            setattr(test_solution, test_name, func)
