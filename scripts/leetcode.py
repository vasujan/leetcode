import inspect
from pathlib import Path
from typing import Any, Callable, Iterable, Self, TypeVar

import attrs
import cattrs

converter = cattrs.Converter()

T = TypeVar("T", bound=int)


@attrs.define
class ListNode[T]:
    val: T
    next: Self | None = None

    @classmethod
    def from_list(cls, values: list[T]) -> Self | None:
        if not values:
            return None
        ln = cls(values[0], None)
        current = ln
        for value in values[1:]:
            current.next = cls(value, None)
            current = current.next
        return ln

    def to_list(self) -> list[T]:
        result = [self.val]
        current = self
        while current.next:
            current = current.next
            result.append(current.val)
        return result

    def __repr__(self):
        next_repr = f"ListNode({self.next.val})" if self.next else "None"
        return f"ListNode(val={self.val}, next={next_repr})"


@attrs.define
class TreeNode[T]:
    val: T
    left: Self | None = None
    right: Self | None = None

    @classmethod
    def from_list(cls, values: list[T]) -> Self | None:
        if not values:
            return None
        root = cls(values[0], None, None)
        queue = [root]
        index = 1
        while queue and index < len(values):
            current = queue.pop(0)
            if index < len(values) and values[index] is not None:
                current.left = cls(values[index], None, None)
                queue.append(current.left)
            index += 1
            if index < len(values) and values[index] is not None:
                current.right = cls(values[index], None, None)
                queue.append(current.right)
            index += 1
        return root

    def to_list(self) -> list[T | None]:
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left) if current.left else result.append(None)
                queue.append(current.right) if current.right else result.append(None)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result


def parse_value(raw: str, typ: type) -> Any:
    value = raw.strip()
    if not value:
        raise ValueError("Empty argument value in test file")
    if value[0] == "[" and value[-1] == "]":
        value = value[1:-1].strip().split(",")
    if value == "null":
        return None
    return converter.structure(value, typ)


def test_case_reader(
    test_file_path: Path | str, func_signature: inspect.Signature | Callable
):
    if isinstance(test_file_path, str):
        test_file_path = Path(test_file_path)

    if callable(func_signature):
        func_signature = inspect.signature(func_signature)
    if not isinstance(func_signature, inspect.Signature):
        raise TypeError("func_signature must be a signature or callable")
    param_count = len(func_signature.parameters)
    if param_count == 0:
        raise ValueError("Function must have parameters to use test cases from file")

    raw_lines = [
        line.strip() for line in test_file_path.read_text().splitlines() if line.strip()
    ]

    if len(raw_lines) % param_count != 0:
        raise ValueError("Test case file does not align with function parameter count")
    test_cases = []

    arg_types = [
        v.annotation for k, v in func_signature.parameters.items() if k != "self"
    ]

    for i in range(0, len(raw_lines), param_count):
        args = raw_lines[i : i + param_count]
        structured_args = [parse_value(arg, typ) for arg, typ in zip(args, arg_types)]
        test_cases.append(structured_args)
    return test_cases


def test_case_writer(output_file_path: Path, outputs: Iterable[Any]) -> Path:
    def serialize_value(value: Any) -> str:
        if value is None:
            return "null"
        if isinstance(value, list) or isinstance(value, tuple):
            inner = ",".join(serialize_value(item) for item in value)
            return f"[{inner}]"
        if isinstance(value, str):
            return f'"{value}"'
        return str(value)

    lines = [serialize_value(output) for output in outputs]
    output_file_path.write_text("\n".join(lines) + ("\n" if lines else ""))
    return output_file_path


class _TestSolutionMethod:
    def __init__(
        self,
        func,
        test_case_file: Path,
        write_output: bool | Path,
        run_tests: bool,
    ):
        self.func = func
        self.test_case_file = test_case_file
        self.write_output = write_output
        self.run_tests = run_tests
        self.signature = inspect.signature(func)
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__
        self.__qualname__ = func.__qualname__
        self.__module__ = func.__module__

    def __get__(self, instance, owner):
        return self.func.__get__(instance, owner)

    def __set_name__(self, owner, name):
        run_name = "run"
        run_specific_name = f"run_{name}"

        def run(self_instance):
            cases = test_case_reader(self.test_case_file, self.signature)
            results = []
            if self.run_tests:
                bound = self.func.__get__(self_instance, owner)
                for args in cases:
                    results.append(bound(*args))
            if self.write_output and self.run_tests:
                output_path = (
                    self.write_output
                    if isinstance(self.write_output, Path)
                    else self.test_case_file.with_name("solution.txt")
                )
                test_case_writer(output_path, results)
            return results

        if not hasattr(owner, run_specific_name):
            setattr(owner, run_specific_name, run)
        if not hasattr(owner, run_name):
            setattr(owner, run_name, run)


def test_solution(
    test_case_file: Path,
    write_output: bool | Path = False,
    run_tests: bool = True,
):
    def decorator(func):
        return _TestSolutionMethod(func, test_case_file, write_output, run_tests)

    return decorator
