class Fruit:
    @classmethod
    def list_fruits(cls) -> None:
        cls = "apple"  # [self-cls-assignment]

    def print_color(self, *colors: str) -> None:
        self = "red"  # [self-cls-assignment]
        color = colors[1]
        print(color)
