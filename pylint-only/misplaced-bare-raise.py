def validate_positive(x: int) -> None:
    if x <= 0:
        raise  # [misplaced-bare-raise]
