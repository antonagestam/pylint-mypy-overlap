class Animal:
    def eat(self, food: object) -> None:
        print(f"Eating {food}")


class Human(Animal):
    def eat(self, food: object) -> None:  # [useless-parent-delegation]
        super().eat(food)
