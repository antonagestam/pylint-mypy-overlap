from typing import Iterable

def find_even_number(numbers: Iterable[int]) -> int:
    for x in numbers:
        if x % 2 == 0:
            break
    return x  # [undefined-loop-variable]
