class BadFormat:
    """__format__ returns <type 'int'>"""

    def __format__(self, format_spec: object) -> int:  # [invalid-format-returned]
        return 1

