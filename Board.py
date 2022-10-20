from Dot import Dot


class Board(Dot):

    def __init__(self) -> None:
        self.board = [[Dot("empty_dot") for _ in range(10)]
                      for _ in range(10)]

    def board_representation(self) -> Dot:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end="")
            print()
