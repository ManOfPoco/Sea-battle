from Dot import Dot


class Ship(Dot):
    def __init__(self, x, y, sigh) -> None:
        super().__init__(sigh)


class TwoDeckShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        super().__init__(sigh)


class ThreeDeckShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        super().__init__(sigh)


class FourDeckShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        super().__init__(sigh)
