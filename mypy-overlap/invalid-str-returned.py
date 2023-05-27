class Str:
    """__str__ returns int"""

    def __str__(self) -> int:  # [invalid-str-returned]
        return 1
