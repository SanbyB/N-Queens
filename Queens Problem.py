import numpy as np

'''
Solution to the N Queens problem for a given board size,
The problem states that given an N*N board place N Queens
from the game of chess onto the board without any of the
Queens being under attack from another Queen.
This solution uses a backtracking algorithm to solve this problem,
which makes it much more time efficient than a naive algorithm 
to solve as the possibilities become exponential.
'''


def place(board, x, y, diag1, diag2):
    '''
    This function implements the placing of a queen
    When a queen is placed, the positions under attack on the board have their values increase by 1
    and the position the queen is placed is changed to n+1
    '''

    n = len(board)

    for i in range(n):

        board[i][y] += 1  # applies the vertical attack to the board

        for j in range(n):  # applies the diagonal attacks to the board
            if diag1[i][j] == diag1[x][y]:
                board[i][j] += 1
            if diag2[i][j] == diag2[x][y]:
                board[i][j] += 1

    board[x][y] = n + 1  # places the queen, the value has to be greater than the number of queens
    #  placed as a position could have the potential to be under attack from n queens


def unplace(board, x, y, diag1, diag2):
    '''
    This function implements the un-placing of a queen when backtracking is needed
    When a queen is placed, the positions under attack on the board have their values increase by 1
    and the position the queen is placed is changed to n+1
    When unplaced we reduce the values under attack by 1, and set the position the queen was in to -1
    '''

    n = len(board)

    for i in range(n):

        board[i][y] -= 1  # removes the vertical attack to the board

        for j in range(n):  # removes the diagonal attacks to the board
            if diag1[i][j] == diag1[x][y]:
                board[i][j] -= 1
            if diag2[i][j] == diag2[x][y]:
                board[i][j] -= 1

    board[x][y] = -1  # removes the queen


def check(x, y, board):
    '''
    checks if a given position [x, y] on the board is safe
    if it is safe: returns True
    else: returns False
    '''
    if board[x][y] == -1:
        return True
    return False


def solutionnq(n, step, board, diag1, diag2):
    if step == n:
        return True

    for i in range(n):
        if check(step, i, board):  # if the position is valid for a queen to be placed
            place(board, step, i, diag1, diag2)  # place a queen
            if solutionnq(n, step + 1, board, diag1, diag2):
                return True
            unplace(board, step, i, diag1, diag2)

    return False


def solvenq(n):
    '''
    sets up the board, and the diag boards which are used to implement the queens attack
    calls the solution function to solve the N Queens problem
    '''
    board = [[-1 for i in range(n)] for i in range(n)]  # sets up n*n board filled with -1

    '''
    diag1 and diag2 are the boards that determine the diagonal attacks of the queen
    '''

    diag1 = [[i + j for i in range(n)] for j in range(n)]

    diag2 = [[i - j for i in range(n)] for j in range(n)]

    step = 0

    if (not solutionnq(n, step, board, diag1, diag2)):
        print("Solution does not exist")
    else:
        printboard(board)


def printboard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == len(board)+1:
                board[i][j] = 'Q'
            else:
                board[i][j] = '_'
    print(np.matrix(board))


solvenq(8)
