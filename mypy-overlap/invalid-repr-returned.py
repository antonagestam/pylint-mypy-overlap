class Repr:
    """__repr__ returns <type 'int'>"""

    def __repr__(self) -> int:  # [invalid-repr-returned]
        return 1
