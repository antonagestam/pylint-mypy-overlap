class Fruit:
    # When returning object or Any:
    # init-is-generator.py:2: error: The return type of "__init__" must be None  [misc]
    def __init__(self, worms: list) -> None:  # [init-is-generator]
        yield from worms


apple = Fruit(["Fahad", "Anisha", "Tabatha"])
