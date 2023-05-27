class BadIndex:
    """__index__ returns a dict"""

    def __index__(self) -> dict[str, str]:  # [invalid-index-returned]
        return {"19": "19"}
