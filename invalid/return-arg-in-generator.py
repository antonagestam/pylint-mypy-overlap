from typing import Iterator

def yield_numbers() -> Iterator[int]:
    for number in range(10):
        yield number
        return "I am now allowed!"  # This was not allowed in Python 3.3 and earlier.

