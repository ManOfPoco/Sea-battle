from Dot import Dot


class Board(Dot):

    def __init__(self) -> None:
        self.board = [[Dot(i, y, "empty_dot") for i in range(10)]
                      for y in range(10)]

    def board_representation(self, hide=False) -> Dot:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if hide:
                    if self.board[i][j].sigh == self.SIGNS.get("enemy_ship"):
                        print(self.board[i][j].SIGNS.get("empty_dot"), end="")
                        continue
                print(self.board[i][j], end="")
            print()
