class BadHash:
    """__hash__ returns dict"""

    def __hash__(self) -> dict:  # [invalid-hash-returned]
        return {}
