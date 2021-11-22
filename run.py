import random
from os import system, name
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X"
current_winner = None
game_running = True


def clear():
    """
    Function to clear the screen
    """
    os.system("cls" if os.name == "nt" else "clear")


# print the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    # change to while loop for until user enter number 1-9
    pinput = int(input("Enter a number 1-9: "))
    if pinput >= 1 and pinput <= 9 and board[pinput-1] == "-":
        board[pinput-1] = current_player
    else:
        print("A player is already in that spot.")


# check for win or tie
def check_hor(board):
    global current_winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        current_winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        current_winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        current_winner = board[6]
        return True


def check_vert(board):
    global current_winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        current_winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        current_winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        current_winner = board[2]
        return True


def check_diag(board):
    global current_winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        current_winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        current_winner = board[2]
        return True


def check_tie(board):
    if "-" not in board:
        print_board(board)
        print("The game ends in a Tie!")
        game_running = False


def check_win():
    if check_hor(board) or check_vert(board) or check_diag(board):
        print(f"{current_winner} has won this game!")


# switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# computer player
def computer_player(board):
    while current_player == "O":
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = "O"
            switch_player()


# Find a way to clean this up
while game_running:
    print_board(board)
    playerInput(board)
    # check_win()
    # check_tie(board)
    switch_player()
    computer_player(board)
    check_win()
    check_tie(board)

# Game doesn't stop after a winner is declared
# Change X, O to a different icon
# Add gameover screen at the end?
# Add menu screen
