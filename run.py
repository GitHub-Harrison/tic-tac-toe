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

# Code for computer player
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

# Code for the human player
class HumanPlayer(Player):
    
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

# Code for the board
def print_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Code for available moves
def available_moves(self):
    moves = []
    for (i, spot) in enumerate(self.board):
        if spot == ' ':
            moves.append(i)
    return moves