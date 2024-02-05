from typing import Callable

MyCustomFn = Callable[[int, int], None]

def plus(a: int, b: int) -> None:
    print(a + b)

def function_executor(fn: MyCustomFn, args: list[int]) -> None:
    fn(*args)

function_executor(plus, [1, 2])
