class Fruit:
    def __init__(self, name: str = "fruit") -> None:
        self.name = name
        print("Creating a {self.name}")


class Apple(Fruit):
    def __init__(self) -> None:  # [super-init-not-called]
        print("Creating an apple")
