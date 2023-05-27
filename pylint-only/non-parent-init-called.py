class Animal:
    def __init__(self) -> None:
        self.is_multicellular = True


class Vertebrate(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.has_vertebrae = True


class Cat(Vertebrate):
    def __init__(self) -> None:
        Animal.__init__(self)  # [non-parent-init-called]
        self.is_adorable = True
