class BadBool:
    """__bool__ returns an int"""

    def __bool__(self) -> int:  # [invalid-bool-returned]
        return 1
