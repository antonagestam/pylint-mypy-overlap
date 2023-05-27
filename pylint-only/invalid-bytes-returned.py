class BadBytes:
    """__bytes__ returns <type 'str'>"""

    def __bytes__(self) -> str:  # [invalid-bytes-returned]
        return "123"
