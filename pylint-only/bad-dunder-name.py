class Apples:
    def _init_(self) -> None:  # [bad-dunder-name]
        pass

    def __hello__(self) -> None:  # [bad-dunder-name]
        print("hello")
