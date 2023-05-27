class BadGetNewArgs:
    """__getnewargs__ returns an integer"""

    def __getnewargs__(self) -> int:  # [invalid-getnewargs-returned]
        return 1
