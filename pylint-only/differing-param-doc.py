def foo(x: int, y: int) -> int:  # [differing-param-doc]
    """A dummy string.

    :param int x: x value.
    :param int z: z value.
    """

    return x + y
