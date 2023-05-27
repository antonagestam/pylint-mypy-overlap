class BadGetNewArgsEx:
    """__getnewargs_ex__ returns tuple with incorrect arg length"""

    def __getnewargs_ex__(self) -> tuple[tuple[int], dict[str, str], int]:  # [invalid-getnewargs-ex-returned]
        return ((1,), dict(x="y"), 1)
