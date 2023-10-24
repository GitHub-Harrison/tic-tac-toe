import random
import math
import time
import os
import sys


def clear():
    """
    Function which is supposed to clear the terminal to
    make it more user friendly
    """
    os.system("cls" if os.name == "nt" else "clear")


class Player:
    """
    Class for basic player functions
    """

    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        """
        for players to get their next move
        """
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
            print()
            square = input(self.letter + "'s turn. Enter move (1-9): ")
            try:
                val = int(square)
                if val < 1 or val > 9:
                    raise ValueError
                val -= 1 # adjust user input to 0-8 range
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Please try again.")
        return val


def htp():
    """
    How to play section accessed from the main menu
    similar to the about section
    """

    print("\nTic-tac-toe is a simple game, here are the basics:")
    print()
    time.sleep(0.25)
    print("First, the board gets drawn.")
    time.sleep(0.25)
    print("\nSecond, the first player makes their move.")
    time.sleep(0.25)
    print("In this game the human player will always go first.")
    time.sleep(0.25)
    print("\nNext the computer will make their move.")
    time.sleep(0.25)
    print("\nFrom here the players keep alternating moves until")
    time.sleep(0.25)
    print("one of the players has drawn a row of three symbols")
    time.sleep(0.25)
    print("or until no one can win.")
    time.sleep(0.25)
    print("\nIn the case that no one can win the game will end")
    time.sleep(0.25)
    print("in a tie.")
    time.sleep(0.25)
    print("\nRegardless of who wins, once the game has ended you")
    time.sleep(0.25)
    print("can always play again!")
    time.sleep(0.25)

    menu()


def about():
    """
    function to create an about section accessed
    from the main menu, users can return to the main
    menu or access any option the main menu offers
    """

    print("\nTic-tac-toe or noughts and crosses is a")
    time.sleep(0.25)
    print("paper-and-pencil game for two players who take")
    time.sleep(0.25)
    print("turns marking the spaces in a 3x3 grid with X or O.")
    time.sleep(0.25)
    print("\nThe player who succeeds in placing three of their")
    time.sleep(0.25)
    print("letters in a horizontal, vertical or diagonal row is")
    time.sleep(0.25)
    print("the winner.")
    time.sleep(0.25)
    print("\nIf neither player can place 3 in a row the game")
    time.sleep(0.25)
    print("ends in a tie and the players can play again.")
    time.sleep(0.25)

    menu()


def main_menu():
    """
    Function for a main menu making it more obvious
    to users that the code/game has started.
    List of options containing:
    1) Play Game 2) How to play 3) About 4) Exit
    """

    choice = 0
    while choice != "4":

        print("\nWelcome to my Tic-Tac-Toe game!")
        print()
        print("Choose from this menu to continue.")
        print()
        print("1 - Play Game")
        print("2 - How to play")
        print("3 - About")
        print("4 - Exit")
        print()
        choice = input("Enter your choice: ")

        if choice == "1":
            clear()
            print("\nGame Loading...\n")
            time.sleep(1)
            ttt.reset()
            play(ttt, x_player, o_player, print_game=True)
        elif choice == "2":
            clear()
            print("\tHow to play")
            htp()
            time.sleep(1.5)
        elif choice == "3":
            clear()
            print("\tAbout")
            about()
            time.sleep(1.5)
        elif choice == "4":
            print("\nThank you for playing!")
            sys.exit()
        else:
            print("\nPlease enter a valid choice.")
            time.sleep(2)
            clear()


def menu():
    """
    similar to main menu but with only two
    options to return to main menu or play
    game to be called on the about and
    how to play sections
    """

    print("\n")
    print("1 - Return")
    print("2 - Play Game")
    print()
    option = input("Enter your choice: ")

    if option == "1":
        clear()
        print("\nReturning to Main Menu...")
        time.sleep(1)
        main_menu()
    elif option == "2":
        clear()
        print("\nGame Loading...")
        time.sleep(0.8)
        ttt.reset()
        play(ttt, x_player, o_player, print_game=True)
    else:
        print("Please enter a valid option.")
        clear()
        time.sleep(0.8)
        menu()


class TicTacToe:
    """
    Class containing all function required to run the game
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]   # to replicate 3x3 board
        self.current_winner = None   # to keep track of the winner

    def reset(self):
        """
        function to reset the values of the following
        variables
        """
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    # Code for the board
    @staticmethod
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
        num_board = [[str(i + 1) for i in range(j*3, (j+1)*3)] for j in range(3)]
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

    def winner(self, square, letter):
        """
        Function which checks all possible winning
        combonations and returns the result
        """
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False


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
                    time.sleep(1)
                    print(letter + " has won!")
                return letter

            # after the move is made, the player letter switches
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

        time.sleep(2.5)
        clear()
        game.print_board()

    if print_game:
        print("\nIt's a Tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    ttt = TicTacToe()
    main_menu()
