from Board import Board
import Ships


class Player:
    """Class represents Players"""

    def __init__(self, name: str, board: Board) -> None:
        self.name = name.lower()
        self.board = board

    def validate_ship_distance(self, x, y, ship_color):
        x, y = x - 1, y - 1
        for _ in range(3):
            for _ in range(3):
                if not self.board_validation(x, y):
                    y += 1
                    continue
                if self.board.board[x][y].sigh == Ships.Dot.SIGNS.get(ship_color):
                    return False

                y += 1
            x += 1
            y -= 3

        return True

    def validation_putting_ships(self, x, y, ship_type, direction, ship_color) -> bool:
        """Validating putting ships on the board"""

        if ship_type != 1:
            for _ in range(ship_type):
                if not self.board_validation(x, y):
                    return False
                if not self.validate_ship_distance(x, y, ship_color):
                    return False

                x += direction[0]
                y += direction[1]
        else:
            if not self.validate_ship_distance(x, y, ship_color):
                return False

        return True

    def board_validation(self, x: int, y: int) -> bool:
        """Validating if particular Dot on the Board"""

        if x not in range(10) or y not in range(10):
            return False
        return True

    def put_ship(self, ship_type: int, coord_x: int,
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

        if not self.validation_putting_ships(coord_x, coord_y, ship_type,
                                             direction_relation.get(direction),
                                             ship_color):
            return False

        ship = ship_relation.get(ship_type)(coord_x, coord_y, ship_color)

        for _ in range(ship_type):
            self.board.board[coord_x][coord_y] = ship
            if ship_type != 1:
                coord_x += direction_relation.get(direction)[0]
                coord_y += direction_relation.get(direction)[1]

        return True

    def shot(self, x: int, y: int, enemy: Ships) -> bool:
        """Player shot"""

        if self.board_validation(x, y):

            if (x, y,) in self.board.already_fired or \
                    enemy.board.board[x][y].sigh == self.board.SIGNS.get("miss"):
                return False

            elif enemy.board.board[x][y].sigh != self.board.SIGNS.get("empty_dot"):
                enemy_ship = enemy.board.board[x][y]
                enemy_ship.health -= 1

                enemy_ship.parts_to_destroy.append((x, y))

                if enemy_ship.health == 3:
                    enemy_ship.change_dot("three_health")
                    print("Экипаж контужен!!!")

                elif enemy_ship.health == 2:
                    enemy_ship.change_dot("two_health")
                    print("Небольшое возгорание!!!")

                elif enemy_ship.health == 1:
                    enemy_ship.change_dot("one_health")
                    print("ПОЛЫХАЕТ!!!")

                else:
                    enemy_ship.change_dot("destroy")
                    print("УНИЧТОЖИЛ!!!")
                    destroy = enemy_ship.parts_to_destroy

                    for i in range(len(destroy)):
                        for j in range(1):
                            enemy_ship.destroy_effect(destroy[i][j],
                                                      destroy[i][j+1],
                                                      enemy.board.board)
            else:
                enemy.board.board[x][y].change_dot("miss")
                print("Промах...")

            self.board.already_fired.append((x, y))
            return True
        return False
