def small_apple(apple: list[object], length: int) -> None:
    if len(apple) < length:
        raise Exception("Apple is too small!")  # [broad-exception-raised]
    print(f"{apple} is proper size.")
