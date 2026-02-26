import inspect
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterable, TypeVar

import cattrs

from .models import ListNode, TreeNode

converter = cattrs.Converter()
converter.register_structure_hook(ListNode, lambda obj, _: ListNode.from_list(obj))
converter.register_unstructure_hook(ListNode, lambda obj: obj.to_list())
converter.register_structure_hook(TreeNode, lambda obj, _: TreeNode.from_list(obj))
converter.register_unstructure_hook(TreeNode, lambda obj: obj.to_list())


T = TypeVar("T", bound=int)


@contextmanager
def push_pythonpath(path: Path | str):
    if isinstance(path, str):
        path = Path(path)
    assert path.is_dir(), f"Provided path is not a directory: {path}"
    original_pythonpath = sys.path.copy()
    sys.path.insert(0, str(path.expanduser().absolute()))
    try:
        yield
    finally:
        sys.path = original_pythonpath


def parse_value(raw: str, typ: type) -> Any:
    value = raw.strip()
    if not value:
        raise ValueError("Empty argument value in test file")
    if value[0] == "[" and value[-1] == "]":
        value = value[1:-1].strip().split(",")
    if value[0] == '"' and value[-1] == '"':
        value = value[1:-1]
    if value == "null":
        return None
    return converter.structure(value, typ)


def serialize_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, list) or isinstance(value, tuple):
        inner = ",".join(serialize_value(item) for item in value)
        return f"[{inner}]"
    if isinstance(value, str):
        return f'"{value}"'
    return str(value)


def get_func_types(func: Callable) -> tuple[list[type], type | None]:
    if not callable(func):
        raise TypeError("func must be a callable to use test cases from file")

    annotations = func.__annotations__
    param_types = [v for k, v in annotations.items() if k != "return"]
    return_type = annotations.get("return", None)
    return param_types, return_type


def get_test_case_parser_serializer(
    func: Callable,
) -> tuple[Callable[[list[str]], list[Any]], Callable[[Iterable[Any]], list[str]]]:
    param_types, return_type = get_func_types(func)

    def parser(raw_lines: list[str]) -> list[Any]:
        if len(raw_lines) % len(param_types) != 0:
            raise ValueError(
                "Test case file does not align with function parameter count"
            )
        test_cases = []
        for i in range(0, len(raw_lines), len(param_types)):
            args = raw_lines[i : i + len(param_types)]
            structured_args = [
                parse_value(arg, typ) for arg, typ in zip(args, param_types)
            ]
            test_cases.append(structured_args)
        return test_cases

    def serializer(outputs: Iterable[Any]) -> list[str]:
        return [serialize_value(output) for output in outputs]

    return parser, serializer


def read_text_file(test_file_path: Path | str) -> list[str]:
    if isinstance(test_file_path, str):
        test_file_path = Path(test_file_path)
    assert test_file_path.is_file(), f"Test case file not found: {test_file_path}"
    assert test_file_path.exists(), f"Test case file does not exist: {test_file_path}"
    assert test_file_path.suffix in (".txt",), (
        f"Unsupported test case file format: {test_file_path.suffix}"
    )
    raw_lines = [
        line.strip() for line in test_file_path.read_text().splitlines() if line.strip()
    ]
    return raw_lines


class SolutionTester:
    def __init__(
        self,
        solution_dir: Path | str,
        method_name: str | None = None,
        test_cases_file_name: str = "test_cases.txt",
        expected_outputs_file_name: str = "expected_outputs.txt",
        outputs_file_name: str | None = None,
        correct_solution: Callable | None = None,
    ):
        if isinstance(solution_dir, str):
            solution_dir = Path(solution_dir)
        assert solution_dir.is_dir(), (
            f"Provided solution directory is not a directory: {solution_dir}"
        )
        self.solution_dir = solution_dir.expanduser().absolute()
        self.method_name = method_name
        self.test_cases_file_name = test_cases_file_name
        self.expected_outputs_file_name = expected_outputs_file_name
        self.outputs_file_name = outputs_file_name
        self.correct_solution = correct_solution

    def _load_solution_class(self) -> type:
        with push_pythonpath(self.solution_dir):
            from solution import Solution  # type: ignore
        return Solution

    def _get_solution_method(self, Solution: type) -> Callable:
        methods = inspect.getmembers(Solution, predicate=inspect.isfunction)
        if len(methods) == 0:
            raise ValueError("No methods found in Solution class")
        if len(methods) > 1 and self.method_name is None:
            raise ValueError(
                "Multiple methods found in Solution class, unable to determine which one to test. Please specify method_name."
            )
        return (
            getattr(Solution, self.method_name) if self.method_name else methods[0][1]
        )

    def _load_test_cases(
        self,
        parser: Callable[[list[str]], list[Any]],
        provided_test_cases: list[Any] | None,
    ) -> list[Any]:
        if provided_test_cases is not None:
            return provided_test_cases
        test_file_path = self.solution_dir / self.test_cases_file_name
        assert test_file_path.is_file(), f"Test case file not found: {test_file_path}"
        return parser(read_text_file(test_file_path))

    def _load_expected_outputs(
        self,
        parser: Callable[[list[str]], list[Any]],
        provided_expected_outputs: list[Any] | None,
    ) -> list[Any] | None:
        if provided_expected_outputs is not None:
            return provided_expected_outputs
        expected_outputs_file_path = self.solution_dir / self.expected_outputs_file_name
        if not expected_outputs_file_path.exists():
            return None
        return parser(read_text_file(expected_outputs_file_path))

    def _run_single_test(
        self,
        Solution: type,
        func: Callable,
        args: list[Any],
        expected_output: Any | None,
    ) -> tuple[Any, bool]:
        solution = Solution()
        result = func(solution, *args)
        passed = expected_output is None or result == expected_output
        return result, passed

    def _write_outputs(
        self, serializer: Callable[[Iterable[Any]], list[str]], results: list[Any]
    ) -> None:
        if self.outputs_file_name is None:
            return
        outputs_file_path = self.solution_dir / self.outputs_file_name
        outputs_file_path.write_text("\n".join(serializer(results)))

    def run(
        self,
        test_cases: list[Any] | None = None,
        expected_outputs: list[Any] | None = None,
        printer: Callable[[str], None] = print,
    ) -> list[Any]:
        Solution = self._load_solution_class()
        func = self._get_solution_method(Solution)

        func_name = getattr(func, "__name__", repr(func))
        printer(f"Testing method: {func_name}{inspect.signature(func)}")

        parser, serializer = get_test_case_parser_serializer(func)
        test_cases = self._load_test_cases(parser, test_cases)
        expected_outputs = self._load_expected_outputs(parser, expected_outputs)
        if expected_outputs is not None:
            printer(f"Loaded {len(expected_outputs)} expected outputs for comparison")

        if expected_outputs is not None:
            assert len(test_cases) == len(expected_outputs), (
                "Number of test cases does not match number of expected outputs"
            )

        _, return_type = get_func_types(func)
        assert return_type is not None, (
            "Function must have a return type annotation for testing with expected outputs"
        )

        printer("-" * 80)
        results = []
        for i, args in enumerate(test_cases):
            printer(f"Test case {i + 1}: {args}")

            if expected_outputs is not None:
                expected = (
                    expected_outputs[i][0]
                    if isinstance(expected_outputs[i], (list, tuple))
                    else expected_outputs[i]
                )
                expected = converter.structure(expected, return_type)
            elif self.correct_solution is not None:
                expected = self.correct_solution(*args)
            else:
                expected = None

            result, passed = self._run_single_test(Solution, func, args, expected)
            results.append(result)

            printer(f"Output: {result}")
            if not passed:
                printer(f"Failed: expected {expected}, got {result}")
            printer("-" * 80)

        self._write_outputs(serializer, results)
        return results
