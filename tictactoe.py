# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD
symbol = [ " ", "x", "o" ]
def printRow(row):
    board = [0,0,0,
             0,0,0,
             0,0,0]
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    # initialize output to the left border
    # for each square in the row...
    for i in board:
        print (i)
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
pass
def printBoard(board):
    # print the top border
    # for each row in the board...
    # print the row
    # print the next border
    pass
def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    # if so, set it to the player number
    pass
def getPlayerMove():
    player = input("Please state if you are player 1 or 2")
    row = input("Please enter the row number you wish to mark")
    column = input("Please enter the column number you wish to mark")
    if board
    # prompt the user separately for the row and column numbers
    return (0,0) # then return that row and column instead of (0,0)
def hasBlanks(board):
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    return True # if no square is blank, return False
def main():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]# TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
    row,col = getPlayerMove()
    markBoard(board,row,col,player)
    player = player % 2 + 1 # switch player for next turn
    main()
