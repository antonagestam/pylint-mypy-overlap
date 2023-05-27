class Fruit:
    def brew(self, ingredient_name: str) -> None:
        print(f"Brewing a {type(self)} with {ingredient_name}")


class Apple(Fruit):
    ...


class Orange(Fruit):
    def brew(self, flavor: str) -> None:  # [arguments-renamed]
        print(f"Brewing an orange with {flavor}")

fruits: list[tuple[Fruit, str]] = [(Orange(), "thyme"), (Apple(), "cinnamon")]

for fruit, ingredient_name in fruits:
    fruit.brew(ingredient_name=ingredient_name)
