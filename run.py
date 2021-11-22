board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X"
current_winner = None
gameRunning = True

# print the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
print_board(board)

# take player input
def playerInput(board):
    pinput = int(input("Enter a number 1-9: "))
    if pinput >= 1 and pinput <= 9 and board[pinput-1] == "-":
        board[pinput-1] = current_player
    else:
        print("A player is already in that spot.")

# check for win or tie

# switch the player

# check for win or tie again