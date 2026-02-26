import inspect
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Callable, Iterable, TypeVar

import cattrs

from .models import ListNode, TreeNode

converter = cattrs.Converter()

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


converter.register_structure_hook(ListNode, lambda obj, _: ListNode.from_list(obj))
converter.register_unstructure_hook(ListNode, lambda obj: obj.to_list())
converter.register_structure_hook(TreeNode, lambda obj, _: TreeNode.from_list(obj))
converter.register_unstructure_hook(TreeNode, lambda obj: obj.to_list())


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


def test_solution(
    solution_dir: Path | str,
    test_cases_file_name: str = "test_cases.txt",
    method_name: str | None = None,
    test_cases: list[Any] | None = None,
    expected_outputs: list[Any] | None = None,
    expected_outputs_file_name: str | None = None,
    outputs_file_name: str | None = None,
    correct_solution: Callable | None = None,
) -> list[Any]:
    if isinstance(solution_dir, str):
        solution_dir = Path(solution_dir)
    assert solution_dir.is_dir(), (
        f"Provided solution directory is not a directory: {solution_dir}"
    )
    solution_dir = solution_dir.expanduser().absolute()
    with push_pythonpath(solution_dir):
        from solution import Solution  # type: ignore

    methods = inspect.getmembers(Solution, predicate=inspect.isfunction)
    if len(methods) == 0:
        raise ValueError("No methods found in Solution class")
    if len(methods) > 1 and method_name is None:
        raise ValueError(
            "Multiple methods found in Solution class, unable to determine which one to test. Please specify method_name."
        )

    func = getattr(Solution, method_name) if method_name else methods[0][1]
    print(f"Testing method: {func.__name__}{inspect.signature(func)}")

    parser, serializer = get_test_case_parser_serializer(func)
    if test_cases is None:
        test_file_path = solution_dir / test_cases_file_name
        assert test_file_path.is_file(), f"Test case file not found: {test_file_path}"
        test_cases = parser(read_text_file(test_file_path))

    if expected_outputs is None and expected_outputs_file_name is not None:
        expected_outputs_file_path = solution_dir / expected_outputs_file_name
        assert expected_outputs_file_path.is_file(), (
            f"Expected outputs file not found: {expected_outputs_file_path}"
        )
        expected_outputs = parser(read_text_file(expected_outputs_file_path))

    print("-" * 80)
    results = []
    for i, args in enumerate(test_cases):
        print(f"Test case {i + 1}: {args}")
        solution = Solution()
        result = func(solution, *args)
        results.append(result)
        print(f"Output: {result}")
        expected = None
        if expected_outputs is not None:
            expected = expected_outputs[i]
        elif correct_solution is not None:
            expected = correct_solution(*args)
        if expected is not None and result != expected:
            print(f"Failed: expected {expected}, got {result}")
        print("-" * 80)

    if outputs_file_name is not None:
        outputs_file_path = solution_dir / outputs_file_name
        outputs_file_path.write_text("\n".join(serializer(results)))

    return results
