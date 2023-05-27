class Pet:
    def make_sound(self) -> None:
        raise NotImplementedError


class Cat(Pet):  # [abstract-method]
    pass

# mypy doesn't detect this, as Pet is it (arguably correctly) doesn't consider Pet abstract.
Cat()


import abc


class WildAnimal:
    @abc.abstractmethod
    def make_sound(self) -> None:
        pass


class Panther(WildAnimal):  # [abstract-method]
    pass

Panther()
