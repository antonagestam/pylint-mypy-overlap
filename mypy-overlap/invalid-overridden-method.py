from __future__ import annotations


class Insect:
    def eat(self, food: Fruit) -> None:
        ...


class Fruit:
    async def bore(self, insect: Insect) -> None:
        insect.eat(self)


class Apple(Fruit):
    def bore(self, insect: Insect) -> None:  # [invalid-overridden-method]
        insect.eat(self)
