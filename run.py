import math
import random

# Code for the players Human/Computer
class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # for players to get their next move
    def get_move(self, game):
        pass # Continue this later

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass