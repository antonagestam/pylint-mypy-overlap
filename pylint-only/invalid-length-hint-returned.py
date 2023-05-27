class BadLengthHint:
    """__length_hint__ returns non-int"""

    def __length_hint__(self) -> float:  # [invalid-length-hint-returned]
        return 3.0
