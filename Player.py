from Board import Board


class Player:
    def __init__(self, name: str, board: Board) -> None:
        self.name = name
        self.board = board

    def shot(self, x, y) -> bool:
        if x in range(10) and y in range(10):
            self.board.board[x][y].change_dot("miss")
            return True
        return False


pl = Player("Player", Board())
