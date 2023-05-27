from functools import singledispatchmethod


class Board:
    @singledispatchmethod  # [singledispatchmethod-function]
    @staticmethod
    def convert_position(position: object) -> object:
        pass

    @convert_position.register  # [singledispatchmethod-function]
    @staticmethod
    def _(position: str) -> tuple[int, int]:
        position_a, position_b = position.split(",")
        return (int(position_a), int(position_b))

    @convert_position.register  # [singledispatchmethod-function]
    @staticmethod
    def _(position: tuple[int, int]) -> str:
        return f"{position[0]},{position[1]}"
