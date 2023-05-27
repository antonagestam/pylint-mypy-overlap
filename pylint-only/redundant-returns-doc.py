def print_fruits(fruits: object) -> None:  # [redundant-returns-doc]
    """Print list of fruits

    Returns
    -------
        str
    """
    print(fruits)
    return None
