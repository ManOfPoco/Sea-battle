from Dot import Dot


class OneDeckShip(Dot):
    def __init__(self, x, y, sigh) -> None:
        self.health = 1
        super().__init__(x, y, sigh)


class TwoDecksShip(Dot):
    def __init__(self, x, y, sigh) -> None:
        self.health = 2
        super().__init__(x, y, sigh)


class ThreeDecksShip(Dot):
    def __init__(self, x, y, sigh) -> None:
        self.health = 3
        super().__init__(x, y, sigh)


class FourDecksShip(Dot):
    def __init__(self, x, y, sigh) -> None:
        self.health = 4
        super().__init__(x, y, sigh)
