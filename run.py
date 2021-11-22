board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
current_player = "X"
current_winner = None
game_running = True

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
def check_hor(board):
    global current_winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

# switch the player

# check for win or tie again

while game_running:
    print_board(board)
    playerInput(board)