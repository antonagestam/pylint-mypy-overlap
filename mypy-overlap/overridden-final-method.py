from typing import final


class Animal:
    @final
    def can_breathe(self) -> object:
        return True


class Cat(Animal):
    def can_breathe(self) -> object:  # [overridden-final-method]
        pass

