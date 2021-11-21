import math
import random

# Code for the players Human/Computer
class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # for players to get their next move
    def get_move(self, game):
        pass

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
        while not valid_square:
            square = input(self.letter + "'s turn. Enter move (0-8):")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Please try again.")
        return val

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]   # to replicate a 3x3 board 
        self.current_winner = None   # to keep track of the winner

    # Code for the board
    def print_board(self):
        print("\n")
        print("\t     |     |")
        # print("\t  {}  |  {}  |  {}")
        print('\t_____|_____|_____')
        print("\t     |     |")
        # print("\t  {}  |  {}  |  {}")
        print('\t_____|_____|_____')
        print("\t     |     |")
        # print("\t  {}  |  {}  |  {}")
        print("\t     |     |")
        print("\n")

    # Code for available moves
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    # Code to check empty squares
    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        # if valid, make move (assign letter to square)
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    # Below code is not detecing a win
    def winner(self, square, letter):
        # winner if 3 in a row, all winning combos
        solution = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for x in solution:
            if all([spot == letter for spot in x]):
                return True
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()
    letter = "X"   # starting letter
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
            # check for winner
            if game.current_winner:
                if print_game:
                    print(letter + "has won!")
                return letter
            # after the move is made, the player letter switches
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'      
    if print_game:
        print("It's a Tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)   
    # TypeError: play() missing 1 required positional argument: 'o_player'

# New error
#   File "run.py", line 133, in <module>
#     play(g, x_player, o_player, print_game=True)
#   File "run.py", line 96, in play
#     game.print_board()
#   File "run.py", line 49, in print_board
#     print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
# TypeError: 'TicTacToe' object is not subscriptable