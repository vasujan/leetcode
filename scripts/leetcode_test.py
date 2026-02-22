import inspect
from pathlib import Path
from typing import Any, Callable, Iterable


def test_case_reader(
    test_file_path: Path, func_signature: inspect.Signature | Callable | int
):
    def parse_value(raw: str) -> Any:
        value = raw.strip()
        if not value:
            raise ValueError("Empty argument value in test file")
        if value[0] == "[" and value[-1] == "]":
            inner = value[1:-1].strip()
            if not inner:
                return []
            return [parse_value(item) for item in inner.split(",")]
        if value[0] == '"' and value[-1] == '"':
            return value[1:-1]
        if value == "null":
            return None
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    if isinstance(func_signature, inspect.Signature):
        param_count = len(func_signature.parameters)
    elif isinstance(func_signature, int):
        param_count = func_signature
    elif callable(func_signature):
        param_count = len(inspect.signature(func_signature).parameters)
    else:
        raise TypeError("func_signature must be a signature, callable, or int")

    raw_lines = [
        line.strip() for line in test_file_path.read_text().splitlines() if line.strip()
    ]

    if param_count == 0:
        raise ValueError("Function must have parameters to use test cases from file")

    if len(raw_lines) % param_count != 0:
        raise ValueError("Test case file does not align with function parameter count")

    parsed_values = [parse_value(line) for line in raw_lines]
    test_cases = []
    for i in range(0, len(parsed_values), param_count):
        test_cases.append(parsed_values[i : i + param_count])
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
