from Dot import Dot


class Ship(Dot):
    def __init__(self, x, y, sigh) -> None:
        self.parts_to_destroy = list()
        super().__init__(x, y, sigh)

    def board_validation(self, x, y) -> bool:
        if x not in range(10) or y not in range(10):
            return False
        return True

    def destroy_effect(self, x, y, board):
        start_y = y
        x, y = x - 1, y - 1
        for _ in range(3):
            for _ in range(3):
                if not self.board_validation(x, y):
                    y += 1
                    continue
                if board[x][y].sigh == self.SIGNS.get("empty_dot"):
                    board[x][y].sigh = self.SIGNS.get("miss")

                y += 1
            x += 1
            y = start_y


class OneDeckShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        self.health = 1
        super().__init__(x, y, sigh)


class TwoDecksShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        self.health = 2
        super().__init__(x, y, sigh)


class ThreeDecksShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        self.health = 3
        super().__init__(x, y, sigh)


class FourDecksShip(Ship):
    def __init__(self, x, y, sigh) -> None:
        self.health = 4
        super().__init__(x, y, sigh)
