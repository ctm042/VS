from itertools import count
from operator import ne
import os
import sys
import copy
from time import sleep

# function to display the board in "matrix" form
def printBoard(board):
    # print col numbers
    print(" ", end = "")
    for col in range(1, size-1):
        print(col, end = "")
    print()
    for row in range(1, size-1):
        # print row numbers
        print(row, end = "")
        for col in range(1, size-1):
            print(board[row][col], end = '')
        print()

# function to count neigbors of a given cell
def countNeighbors(board, row, col):
    # assume a cell has no neighbors
    neighbors = 0
    # check if surrounding has no living cells
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(not(i==0 and j==0)):
                if board[row + i][col + j] == "*":
                    neighbors += 1
    return neighbors

# gunction to compute the next generation/iteration
def computeNextGen(board):
    # copy the previous board
    nextBoard = copy.deepcopy(board)
    for row in range(1, size-1):
        for col in range(1,size-1):
            neighbors = countNeighbors(board, row, col)
            if (board[row][col] == "*"):
                if(neighbors < 2 or neighbors > 3):
                    nextBoard[row][col] = " "
            elif (neighbors == 3):
                nextBoard[row][col] = "*"
    return nextBoard

### MAIN ###
NUM_GENS = 10

board = []

# read the inpet from the terminnal/command line
for line in sys.stdin:
    # determine the size of the board
    size = len(line) - 1
    # for each row in the matrix, create a list to store it's contents
    board.append([])
    for c in range(size):
        board[len(board)-1].append(line[c])

os.system("cls")
print("Gen 0")
printBoard(board)
for gen in range(NUM_GENS):
    sleep(1)
    os.system("cls")
    print(f"Gen {gen + 1}")
    board = computeNextGen(board)
    printBoard(board)