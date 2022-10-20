from Board import Board
import Ships


class Player:
    """Class represent Player"""

    def __init__(self, name: str, board: Board) -> None:
        self.name = name
        self.board = board
    
    def validation_putting_ships(self, x, y, ship_type, direction) -> bool:
        """Validating putting ships on the board"""

        direction_relation = {
            "left": (0, -1), "right": (0, 1),
            "up": (-1, 0), "down": (1, 0),
            "налево": (0, -1), "направо": (0, 1),
            "вверх": (-1, 0), "вниз": (1, 0),
        }

        for _ in range(ship_type):
            if not self.board_validation(x, y):
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

        board_copy = self.board.board.copy()

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

        ship_color = "secondplayer_ship" \
            if self.name.lower() == "computer" else "my_ship"

        ship = ship_relation.get(ship_type)(coord_x, coord_y, ship_color)

        if not self.validation_putting_ships(coord_x, coord_y,
                                             ship_type, direction):
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
print()
pl.put_ships_manually(1, 5, 5, "вверх")
pl.board.board_representation()
print()
pl.put_ships_manually(4, 5, 5, "налево")
pl.board.board_representation()
print()
print(type(pl.board.board[5][5]))
# pl.shot(1, 1)
# pl.board.board_representation()
            # self.board.board[coord_x][coord_y] = ship
            # coord_x += direction_relation.get(direction)[0]
            # coord_y += direction_relation.get(direction)[1]