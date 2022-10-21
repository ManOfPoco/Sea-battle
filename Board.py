from Dot import Dot


class Board(Dot):

    def __init__(self) -> None:
        self.board = [[Dot(i, j, "empty_dot") for i in range(10)]
                      for j in range(10)]
        self.already_fired = list()

    def board_representation(self, hide=False) -> Dot:

        print(end="   ")
        for i in range(10):
            print(i, end=" ")
        print()
        for i in range(len(self.board)):
            print(i, end=" ")
            for j in range(len(self.board[i])):
                if hide:
                    if self.board[i][j].sigh == self.SIGNS.get("enemy_ship"):
                        print(self.board[i][j].SIGNS.get("empty_dot"), end="")
                        continue
                print(str(self.board[i][j].sigh).lstrip(), end="")
            print()
        print()
