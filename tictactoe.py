# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD
symbol = [ " ", "x", "o" ]
def printRow(row):
    completeRow= "|"
    for holder in row:
        if holder == 0:
            completeRow += ("   |")
        if holder == 1:
            completeRow +=(" x |")
        if holder == 2:
            completeRow +=(" o |")
    completeRow += ("\n+-----------+")
    print(completeRow)
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)
    # print the top border
    # for each row in the board...
    # print the row
    # print the next border
def markBoard(board, row, col, player):
    if hasBlanks(board):
        row = int(row)
        col = int(col)
    if player == 1:
        board[col][row] = 1
    elif player == 2:
        board[col][row] = 2
    else:
        print("This square is full")
        return(False)
    # check to see whether the desired square is blank
    # if so, set it to the player number
    
def getPlayerMove():
    row,col = input("Please enter the row and the the column separated by a comma of the position you want to play: ").split(",") # prompt the user separately for the row and column numbers
    return (row,col) # then return that row and column instead of (0,0)
def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0
                return(True)
            else:
                continue
            return(False)
    # for each row in the board...
    # for each square in the row...
    # check whether the square is blank
    # if so, return True
    # if no square is blank, return False
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

