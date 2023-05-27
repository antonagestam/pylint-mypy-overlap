class FruitBasket:
    def __init__(self, fruits: list[str]) -> None:
        self.fruits = fruits

    def __len__(self) -> int:  # [invalid-length-returned]
        return -len(self.fruits)
