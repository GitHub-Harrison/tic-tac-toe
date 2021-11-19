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
        square = random.choice(game.available_moves())
        return square

# Code for the human player
class HumanPlayer(Player):
    
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        While not valid_square:
            square = input(self.letter + "'s turn. Enter move (0-8):")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Please try again.")
        return val

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

def empty_squares(self):
    return " " in self.board

def num_empty_squares(self):
    return self.board.count(" ")

def make_move(self, square, letter):
    # if valid, make move (assign letter to square)
    if self.board[square] == " ":
        self.board[square] = letter
        return True
    return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = "X" # starting letter

    while game.empty_squares():
        # get the move from the player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(" ")
                
            # after the move is made, the player letter switches
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'