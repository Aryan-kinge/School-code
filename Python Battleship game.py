from random import randint

board = []
var = 'x'

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(10):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row - 1 and guess_col == shi-+++++++++_col - 1:
        print("Congratulations! You sank my battleship!")
        break

    else:
        if guess_row not in range(6) or \
                guess_col not in range(6):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == var + 1:
            print( "You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if (turn == 11):
            print("Game Over")
        print_board(board)