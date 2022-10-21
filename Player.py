from Board import Board
import Ships


class Player:
    """Class represent Player"""

    def __init__(self, name: str, board: Board) -> None:
        self.name = name.lower()
        self.board = board

    def validate_ship_distance(self, x, y, ship_color):
        x, y = x - 1, y - 1
        for _ in range(3):
            for _ in range(3):
                if self.board.board[x][y].sigh == Ships.Dot.SIGNS.get(ship_color):
                    return False

                y += 1
            x += 1
            y -= 3

        return True

    def validation_putting_ships(self, x, y, ship_type, direction, ship_color) -> bool:
        """Validating putting ships on the board"""

        direction_relation = {
            "left": (0, -1), "right": (0, 1),
            "up": (-1, 0), "down": (1, 0),
            "налево": (0, -1), "направо": (0, 1),
            "вверх": (-1, 0), "вниз": (1, 0),
        }

        for _ in range(ship_type):
            if not self.board_validation(x, y) or \
               not self.validate_ship_distance(x, y, ship_color):
                return False

            x += direction_relation.get(direction)[0]
            y += direction_relation.get(direction)[1]

        return True

    def board_validation(self, x: int, y: int) -> bool:
        """Validating if particular Dot on the Board"""

        if x not in range(10) or y not in range(10):
            return False
        return True

    def put_ships_manually(self, ship_type: str, coord_x: int,
                           coord_y: int, direction: str = None) -> bool:
        """Putting ships on the Board"""

        ship_relation = {
            1: Ships.OneDeckShip, 2: Ships.TwoDecksShip,
            3: Ships.ThreeDecksShip, 4: Ships.FourDecksShip
        }

        direction_relation = {
            "left": (0, -1), "right": (0, 1),
            "up": (-1, 0), "down": (1, 0),
            "налево": (0, -1), "направо": (0, 1),
            "вверх": (-1, 0), "вниз": (1, 0),
        }

        ship_color = "enemy_ship" \
            if self.name == "computer" else "my_ship"

        ship = ship_relation.get(ship_type)(coord_x, coord_y, ship_color)

        if not self.validation_putting_ships(coord_x, coord_y,
                                             ship_type, direction, ship_color):
            return False

        for _ in range(ship_type):
            self.board.board[coord_x][coord_y] = ship
            coord_x += direction_relation.get(direction)[0]
            coord_y += direction_relation.get(direction)[1]

    def shot(self, x, y) -> bool:
        """Player shot"""

        if self.board(x, y):

            if self.board.board[x][y].sigh == self.board.SIGNS.get("miss") or \
               self.board.board[x][y].sigh == self.board.SIGNS.get("hit"):
                return False
            elif self.board.board[x][y].sigh != self.board.SIGNS.get("empty_dot"):
                self.board.board[x][y].change_dot("hit")
            else:
                self.board.board[x][y].change_dot("miss")

            return True
        return False


pl = Player("Player", Board())
pl.board.board_representation()
print()
pl.put_ships_manually(4, 4, 6, "left")
pl.board.board_representation()
print()

cp = Player("Computer", Board())
cp.put_ships_manually(4, 4, 6, "left")
cp.board.board_representation()
print()
