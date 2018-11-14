import random
board = [" " for x in range(10)]


def WhatIsPlayer():
    global compchar
    rnd = random.randint(0, 1)
    if rnd == 0:
        playerchar = "O"
        compchar = "X"
        return playerchar
    else:
        playerchar = "O"
        compchar = "X"
        return compchar


global playerchar1
playerchar1 = WhatIsPlayer()


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == " "


def printBoard(board):
    print("   ¦   ¦")
    print(" " + board[1] + " ¦ " + board[2] + " ¦ " + board[3])
    print("   ¦   ¦")
    print("-----------")
    print("   ¦   ¦")
    print(" " + board[4] + " ¦ " + board[5] + " ¦ " + board[6])
    print("   ¦   ¦")
    print("-----------")
    print("   ¦   ¦")
    print(" " + board[7] + " ¦ " + board[8] + " ¦ " + board[9])
    print("   ¦   ¦")


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or \
            (bo[4] == le and bo[5] == le and bo[6] == le) or \
            (bo[1] == le and bo[2] == le and bo[3] == le) or \
            (bo[1] == le and bo[4] == le and bo[7] == le) or \
            (bo[2] == le and bo[5] == le and bo[8] == le) or \
            (bo[3] == le and bo[6] == le and bo[9] == le) or \
            (bo[1] == le and bo[5] == le and bo[9] == le) or \
            (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        try:
            pick = int(input("Please pick a cell between 1 and 9 where you want to place your character"))
            pick = int(pick)
            if pick > 0 and pick < 10:
                insertLetter(playerchar1, pick)
                run = False
            else:
                print("Please enter a number between 1 and 9!")
        except:
            print("Please enter a number!")


def compMove():
    pass


def selectRandom(board):
    pass


def isBoardFull(board1, let, let1):
    return (board1[7] == let or let1 and board1[8] == let or let1 and board[9] == let or let1) or \
           (board1[4] == let or let1 and board1[5] == let or let1 and board[6] == let or let1) or \
           (board1[1] == let or let1 and board1[2] == let or let1 and board[3] == let or let1) or \
           (board1[1] == let or let1 and board1[4] == let or let1 and board[7] == let or let1) or \
           (board1[2] == let or let1 and board1[5] == let or let1 and board[8] == let or let1) or \
           (board1[3] == let or let1 and board1[6] == let or let1 and board[9] == let or let1) or \
           (board1[1] == let or let1 and board1[5] == let or let1 and board[9] == let or let1) or \
           (board1[3] == let or let1 and board1[5] == let or let1 and board[7] == let or let1)

def main():
    print("Welcome to Toc Tac Toe!")
    printBoard(board)
    again = True
    print("Now you will be assigned a letter!")
    print("Your character is", playerchar1)
    if not isWinner(board, compchar):
        if isBoardFull(board, "X", "O"):
            playerMove()
            print(printBoard(board))
        else:
            print("Sorry it was a tie!")
            again = str(input("Do you want to play again? Yes or No?"))
            while again:
                if again == "Yes" or "yes":
                    again = False
                elif again == "No" or "no":
                    print("Ok sure, but come and play again soon!")
                    break
                else:
                    again = str(input("Please write Yes or No!"))

    else:
        print("Sorry, The computer has won this time!")
        again = str(input("Do you want to play again? Yes or No?"))
        while again:
            if again == "Yes" or "yes":
                again = False
            elif again == "No" or "no":
                print("Ok sure, but come and play again soon!")
                again = False
                break
            else:
                again = str(input("Please write Yes or No!"))


while True:
    main()