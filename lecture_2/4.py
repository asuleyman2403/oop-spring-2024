from typing import Callable

def plus(a: int, b: int) -> None:
    print(a + b)

def function_executor(fn: Callable[[int, int, int], None], args: list[int]) -> None:
    fn(*args)

function_executor(plus, [1, 2])
