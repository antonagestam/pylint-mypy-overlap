class Soup:
    @staticmethod
    def temp() -> None:
        print("Soup is hot!")


class TomatoSoup(Soup):
    @staticmethod
    def temp() -> None:
        super.temp()  # [super-without-brackets]
        print("But tomato soup is even hotter!")
