import random
import math
import time
import os


class Player:
    """
    Class for basic player functions
    """

    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # for players to get their next move
    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    """
    Class that controls the computer player functions and
    allows the computer to make random moves on the board
    """
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """
    Human player class that controls everything related to
    the users input
    """
    
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        """
        get_move allows the player to make a move and checks if
        the move the player wants is an available move as well as
        checking the user input is correct
        """
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


def main_menu():
    """
    Function for a main menu making it more obvious
    to users that the code/game has started.
    List of options containing: 
    1) Play Game 2) How to play 3) About 4) Exit
    """
    choice = 0
    while choice != "4":

        print("\n Welcome to my Tic-Tac-Toe game!")
        print()
        print("Choose from this menu to continue.")
        print()
        print("1 - Play Game")
        print("2 - How to play")
        print("3 - About")
        print("4 - Exit")
        print()
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                TicTacToe()
            elif choice == "2":
                pass # Create how to play section
            elif choice == "3":
                pass # Create about section
            elif choice == "4":
                print("Thanks for playing!")
        except ValueError:
            print("Please enter a valid choice.")


class TicTacToe:
    """
    Class containing all function required to run the game
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]   # to replicate a 3x3 board 
        self.current_winner = None   # to keep track of the winner

    # Code for the board
    def make_board():
        """
        Function that creates the basic board layout 3x3 square
        """
        return [" " for _ in range(9)]

    def print_board(self):
        """
        Creates the vertical breaks between the columns within
        the board
        """
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print(" | " + " | ".join(row) + " | ")

    @staticmethod
    def print_board_number():
        """
        Function to print numbers allowing users to see
        where they can move to
        """
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print(" | " + " | ".join(row) + " | ")

    # Code for available moves
    def available_moves(self):
        """
        Function to check all possible available
        moves left on the board
        """
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    # Code to check empty squares
    def empty_squares(self):
        """
        function to check what spots are
        empty squares
        """
        return " " in self.board

    def num_empty_squares(self):
        """
        This function is to check the number
        of empty spots on the board
        """
        return self.board.count(" ")

    def make_move(self, square, letter):
        """
        If the move given is a valid option,
        the move will be made
        """
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    # Below code is not detecing a win
    def winner(self, square, letter):
        """
        Function which checks all possible winning
        combonations and returns the result
        """
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def clear():
        """
        Function which is supposed to clear the terminal to
        make it more user friendly
        """
        os.system("cls" if os.name == "nt" else "clear")


def play(game, x_player, o_player, print_game=True):
    """
    Main function that controls the running game
    """

    if print_game:
        game.print_board_number()

    # starting letter
    letter = "X"   
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
                    print(letter + " has won!")
                return letter

            # after the move is made, the player letter switches
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
        
        time.sleep(1)

    if print_game:
        print("It's a Tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    ttt = TicTacToe()
    main_menu()
    play(ttt, x_player, o_player, print_game=True)   
