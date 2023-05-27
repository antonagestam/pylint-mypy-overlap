class Animal:
    def run(self, distance: int = 0) -> None:
        print(f"Ran {distance} km!")


class Dog(Animal):
    def run(self, distance: int) -> None:  # [signature-differs]
        super(Animal, self).run(distance)
        print("Fetched that stick, wuff !")
