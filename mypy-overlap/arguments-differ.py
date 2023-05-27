class Drink:
    def mix(self, fluid_one: int, fluid_two: int) -> int:
        return fluid_one + fluid_two


class Cocktail(Drink):
    def mix(self, fluid_one: int, fluid_two: int, alcoholic_fluid_one: int) -> int:  # [arguments-differ]
        return fluid_one + fluid_two + alcoholic_fluid_one


class Car:
    tank = 0

    def fill_tank(self, gas: int) -> None:
        self.tank += gas


class Airplane(Car):
    kerosene_tank = 0

    def fill_tank(self, gas: int, kerosene: int) -> None:  # [arguments-differ]
        self.tank += gas
        self.kerosene_tank += kerosene
