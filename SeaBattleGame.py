from Board import Board
from Player import Player
from random import choice, choices


class SeaBattleGame:
    def __init__(self, player: Player, computer: Player) -> None:
        self._player = player
        self._computer = computer
        self._round = 1

    def check_end_game(self) -> bool:
        if self._player.board.ships_count() == 20 or \
                self._computer.board.ships_count() == 20:
            return True
        return False

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

        is_autoplacement = input("Do you want to place ships automatically or manually? a(automatically) / m(manually): ")
        if is_autoplacement == "a":
            self.ship_placement_automatically(self._player)
        else:
            self.ship_placement_manually()
        self.ship_placement_automatically(self._computer)

        while not self.check_end_game():
            self._player.board.board_representation()
            self._computer.board.board_representation(hide=True)

            turn_to_shot = self.check_order()
            print(f"Now {turn_to_shot.name} turn")
            self.game_round(turn_to_shot)

        self.end_game()

    def check_order(self):
        self._round += 1
        return self._player \
            if self._round % 2 == 0 else self._computer

    def get_position(self, auto=False):
        while True:
            try:
                if auto:
                    coords = range(10)
                    coord_x, coord_y = choices(coords, k=2)
                else:
                    print(f"Enter position x and y separated by a space to put ship on the deck")
                    self._player.board.board_representation()
                    coord_x, coord_y = map(int, input().split())
            except ValueError:
                print("Please Enter correct value")
                continue
            break
        return coord_x, coord_y

    def get_direction(self, auto=False):

        direction_various = ("up", "down", "left", "right",
                             "вверх", "вниз", "налево", "направо")

        while True:
            if auto:
                direction = choice(direction_various[0:4])
                break
            else:
                print(f"Enter direction to put ship on the deck",
                      f"\nAvaiable directions: {direction_various}")
                self._player.board.board_representation()

                direction = input()
                if direction in direction_various:
                    break

        return direction

    def ship_placement_manually(self):
        ships_remained = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

        while ships_remained:
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

            ship_size = ships_remained.pop(ships_remained.index(ship_choose))

            coord_x, coord_y = self.get_position()

            if ship_size > 1:
                direction = self.get_direction()
                is_putted = self._player.put_ship(ship_size, coord_x,
                                                  coord_y, direction)
            else:
                is_putted = self._player.put_ship(ship_size, coord_x,
                                                  coord_y)

            if is_putted is False:
                print("You can't put a ship there")
                ships_remained.append(ship_size)
                continue

            self._player.board.board_representation()

    def ship_placement_automatically(self, player: Player):
        ships_remained = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        while ships_remained:

            ship_size = ships_remained.pop()

            coord_x, coord_y = self.get_position(auto=True)
            if ship_size > 1:
                direction = self.get_direction(auto=True)
                is_putted = player.put_ship(ship_size, coord_x,
                                            coord_y, direction)
            else:
                is_putted = player.put_ship(ship_size, coord_x,
                                            coord_y)

            if is_putted is False:
                ships_remained.append(ship_size)
                continue

    def game_round(self, player: Player):

        if player.name == self._computer.name:
            coordto_fire_x, coordto_fire_y = choices(range(10), k=2)
        else:
            while True:
                try:
                    coordto_fire_x, coordto_fire_y = map(int, input("Enter position x and y separated by a space to shot: ").split())
                except ValueError:
                    print("Not valid position, try again please")
                    continue
                break

        enemy_to_shot = self._computer \
            if player == self._player else self._player

        result_of_shot = player.shot(coordto_fire_x,
                                     coordto_fire_y, enemy_to_shot)

        if result_of_shot is False:
            if not player.name == self._computer.name:
                print("You can't fire there")
            self.game_round(player)

    def end_game(self):
        if self._player.board.ships_count() == 20:
            print("""================================================================================================================
                                                                            
                                            ░██╗░░░░░░░██╗██╗███╗░░██╗
                                            ░██║░░██╗░░██║██║████╗░██║
                                            ░╚██╗████╗██╔╝██║██╔██╗██║
                                            ░░████╔═████║░██║██║╚████║
                                            ░░╚██╔╝░╚██╔╝░██║██║░╚███║
                                            ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
================================================================================================================""")
        else:
            print("""================================================================================================================
                                    ██████╗░███████╗███████╗███████╗░█████╗░████████╗
                                    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝
                                    ██║░░██║█████╗░░█████╗░░█████╗░░███████║░░░██║░░░
                                    ██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══██║░░░██║░░░
                                    ██████╔╝███████╗██║░░░░░███████╗██║░░██║░░░██║░░░
                                    ╚═════╝░╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
================================================================================================================""")


seabattle = SeaBattleGame(Player("Player", Board()),
                          Player("Computer", Board()))

seabattle.start_game()
