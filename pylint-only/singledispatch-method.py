from functools import singledispatch


class Board:
    @singledispatch  # [singledispatch-method]
    @classmethod
    def convert_position(cls, position: object) -> object:
        pass

    @convert_position.register  # [singledispatch-method]
    @classmethod
    def _(cls, position: str) -> tuple[int, int]:
        position_a, position_b = position.split(",")
        return (int(position_a), int(position_b))

    @convert_position.register  # [singledispatch-method]
    @classmethod
    def _(cls, position: tuple[int, int]) -> str:
        return f"{position[0]},{position[1]}"
