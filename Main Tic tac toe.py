from typing import Any, Union

board = [" " for x in range(10)]
import random
playerchar = random.randint(0, 1)


def WhatIsPlayer():
    global playerchar
    if playerchar == 0:
        compchar = 1
        return compchar

    elif playerchar == 1:
        compchar = 0
        return compchar


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
    return  (bo[7] == le and bo[8] == le and bo[9] == le) or \
         (bo[4] == le and bo[5] == le and bo[6] == le) or \
         (bo[1] == le and bo[2] == le and bo[3] == le) or \
         (bo[1] == le and bo[4] == le and bo[7] == le) or \
         (bo[2] == le and bo[5] == le and bo[8] == le) or \
         (bo[3] == le and bo[6] == le and bo[9] == le) or \
         (bo[1] == le and bo[5] == le and bo[9] == le) or \
         (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    pick = int(input("Please pick a cell between 1 and 9 where you want to place your character"))
    pass



def compMove():
    pass

def selectRandom(board):
    pass

def isBoardFull(board):
    pass

def main():
    global playerchar
    print("Welcome to Toc Tac Toe!")
    printBoard(board)
    print("Now you will be assigned a letter!")
    print("Your character is ", playerchar)
    WhatIsPlayer()
    if not isWinner(board, playerchar):
        playerMove()
        print(printBoard(board))
    else:
        print("Sorry, The computer has won this time!")
        again = str(input("Do you want to play again? Yes or No?"))
        while again == True:
            if again == "Yes" or "yes":
                again = False
            elif again == "No" or "no":
                 print("Ok sure, but come and play again soon!")
                 again = False
                 break
            else:
                again = str(input("Please write Yes or No!"))



main()

