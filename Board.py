from Dot import Dot


class Board(Dot):

    def __init__(self) -> None:
        self.board = [[Dot(i, y, "empty_dot") for i in range(10)]
                      for y in range(10)]

    def board_representation(self) -> Dot:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end="")
            print()
