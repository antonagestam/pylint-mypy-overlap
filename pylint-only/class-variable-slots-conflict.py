class Person:
    # +1: [class-variable-slots-conflict, class-variable-slots-conflict, class-variable-slots-conflict]
    __slots__ = ("age", "name", "say_hi")
    name = None

    def __init__(self, age: int, name: str) -> None:
        self.age = age
        self.name = name

    @property
    def age(self) -> int:
        return self.age

    def say_hi(self) -> None:
        print(f"Hi, I'm {self.name}.")
