import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self) -> None:
        pass


sheep = Animal()
