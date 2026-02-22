import random
from contextlib import contextmanager
from time import perf_counter_ns
from typing import Any, Generator


@contextmanager
def timer(label: str) -> Generator[Any, Any, Any]:
    """
    A context manager that prints the time taken to execute the code inside it.

    Parameters
    ----------
    label : str
        The label to print along with the time taken.
    """
    start = perf_counter_ns()
    try:
        yield
    finally:
        end = perf_counter_ns()
        print(f"{label}: {(end - start) / 1e3:.3f} ms")


def create_random_sorted_array(
    n: int, lowest_step: int = 1, highest_step: int = 10
) -> list[int]:
    sorted_array: list[int] = list()

    for i in range(n):
        val = random.randint(lowest_step, highest_step)
        if i > 0:
            val += sorted_array[-1]
        sorted_array.append(val)

    return sorted_array
