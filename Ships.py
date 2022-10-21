from Dot import Dot


class Ship(Dot):
    def __init__(self, x, y, sigh) -> None:
        super().__init__(x, y, sigh)

    def board_validation(self, x, y) -> bool:
        if x not in range(10) or y not in range(10):
            return False
        return True

    def check_nearest_dots(self, x, y, board):
        start_x, start_y = x, y
        dct = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}

        for i in range(4):
            for j in range(1):
                if not self.board_validation(x, y):
                    x, y = start_x, start_y
                    continue
                print(dct.get(i))
                if board[start_x][start_y].sigh == board[x][y].sigh:
                    self.destroy_effect(start_x, start_y, board)


    def destroy_effect(self, x, y, board):
        start_x, start_y = x, y
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
        self.check_nearest_dots(start_x, start_y, board)


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
