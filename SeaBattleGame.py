from Board import Board
from Player import Player
from random import choice


class SeaBattleGame:
    def __init__(self, player: Player, computer: Player) -> None:
        self._player = player
        self._computer = computer

    def check_end_game(self) -> bool:
        pass

    def start_game(self) -> None:
        print(input("""
|=|__________|=||-------------------------------------------------------------------------=------------------------
|=|__________________XXX
|=|_____________________X
|=|_____________________XXXXXXXXXXXXX
|=|_____________________XXX___X__X_XXXX
|=|_____________________XXX___XXXX___XX
|=|_____________________XXX__XXXXX___XX
|=|_____________________XXX__XXXXX___X
|=|_____________________XXXXXX__XX___X
|=|_____________________X_________XXXX
|=|_____________XXXXXXXXXXXXX
|=|_____________XX___________XX
|=|______________X____________X
|=|______________X_____________X
|=|_______________X____________X
|=|_______________X____________X_XX
|=|_______________X__XXXXXXXXXXXXXXX
|=|_____XXXXXXXXXXXXXX______________X                                   PRESS
|=|_____XX____________X_____XXXXXXXXXXXXXXXX                            Enter
|=|______X______XXXXXXXXXXXXXX______________X                          TO START
|=|______XX_____XX___________X______________XX
|=|_______X______X____________X______________X
|=|_______X______XX___________X_____________X
|=|_______X_______¶___________X_____________XX
|=|______XX_______¶___________XX____________X
|=|___________X_X_XX________XXX_____XXXXXXXX_____XXX
|=|___________X_X_XXXXXXXXXXX_XXXXXXX_______XXXXX__XX
|=|XXXXXX_____X_X______XX_X_______X_XXXXXXXXX___XXXXX
|=|XX___XXXXXXXXX______XX_X____XXXXXXX________XX
|=|__XX________XXXXXXXXXXXXXXXXXX____XX______X
|=|____X____________________________XX_X____X
|=|_____X_____XXX_____XX_____XXX_____XXX___XX
|=|______X___XX_XX___XX_X____X_XX__________X
|=|______XX____XX_____XXX_____XX__________XX
|=|_______XX_____________________________XX
|=|________XX___________________________XX
|=|_________XX________________________XXX
|=|___________|=|--------------------------------------------------------------------------------------------------"""))

        self.ship_placement(self._player)
        self.ship_placement(self._computer)

        # while self.check_end_game():
        #     self.game_round()

    def ship_placement(self, player: Player):
        ships_remained = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

        while ships_remained:
            if player.name == "computer":
                ship_choose = choice(ships_remained)
            else:
                try:
                    print(f"Ships remained {ships_remained}",
                          f"\nEnter a ship to put on the deck")
                    ship_choose = int(input())
                except ValueError:
                    print("Please Enter correct value")
                    continue

            if ship_choose not in ships_remained:
                print("Please Enter correct value")
                continue

            ship = ships_remained.pop(ships_remained.index(ship_choose))

            while True:
                try:
                    print(f"Enter position x and y separated by a space to put ship on the deck")
                    player.board.board_representation()
                    coord_x, coord_y = map(int, input().split())
                    break
                except ValueError:
                    print("Please Enter correct value")
                    continue

            if ship != 1:
                direction_list = ("up", "down", "left", "right",
                                  "вверх", "вниз", "налево", "направо")
                while True:
                    print(f"Enter direction to put ship on the deck",
                          f"\nAvaiable directions: {direction_list}")

                    direction = input()
                    if direction in direction_list:
                        break

                is_putted = player.put_ships_manually(ship, coord_x,
                                                      coord_y, direction)


            is_putted = player.put_ships_manually(ship, coord_x, coord_y)


            # if is_putted:
            #     for i in range(len(self._player.board.board)):
            #         for j in range(len(self._player.board.board[i])):
            #             print(self._player.board.board[i][j], end="")
            #         print()

    def game_round(self):
        pass

    def end_game(self):
        pass


seabattle = SeaBattleGame(Player("Player", Board()),
                          Player("Computer", Board()))

seabattle.start_game()
