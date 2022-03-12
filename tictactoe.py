"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    numberOfMoves = 0
    numberOfEmptyCells = 0
    for i in range(2):
        for j in range(2):
            numberOfMoves+=1
            if(numberOfMoves==10):
                currentTurnNumber = abs(9-numberOfEmptyCells)+1
                XTurn = currentTurnNumber%2!=0
                if (XTurn):
                    return X
                else:
                    return O
                return "END"
            if(board[i][j]==EMPTY):
                numberOfEmptyCells+=1



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setOfPossibleMoves = []
    numberOfMoves = 0
    oddTurn = numberOfMoves % 2 != 0
    for i in range(2):
        for j in range(2):
            numberOfMoves += 1
            if (numberOfMoves == 10):
                return setOfPossibleMoves
            if (board[i][j] == EMPTY):
                setOfPossibleMoves.append((i,j))


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copiedBoard = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    actionSign = player(copiedBoard)
    copiedBoard[i][j] = actionSign
    return copiedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
