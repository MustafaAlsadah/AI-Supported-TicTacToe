"""
Tic Tac Toe Player
"""
import copy
import math
from random import random
import random

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
    """
    Returns player who has the next turn on a board.
    """
    # numberOfMoves = 0
    # numberOfEmptyCells = 0
    # for i in range(2):
    #     for j in range(2):
    #         numberOfMoves+=1
    #         if(numberOfMoves==10):
    #             currentTurnNumber = abs(9-numberOfEmptyCells)+1
    #             XTurn = currentTurnNumber%2!=0
    #             if (XTurn):
    #                 return X
    #             else:
    #                 return O
    #             return "END"
    #         if(board[i][j]==EMPTY):
    #             numberOfEmptyCells+=1
    #

    X_count = 0
    O_count = 0
    EMPTY_count = 0

    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)
        EMPTY_count += row.count(EMPTY)

    # If X has more squares than O, its O's turn:
    if X_count > O_count:
        return O

    # Otherwise it is X's turn:
    else:
        return X


def actions(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves


class InvalidActionError:
    pass


def result(board, action):
    if action == 0:
        # action = (0,0)
        print("LL")
    i = action[0]
    j = action[1]

    # Check if move is valid:
    if i not in [0, 1, 2] or j not in [0, 1, 2]:
        raise InvalidActionError(action, board, 'Result function given an invalid board position for action: ')
    elif board[i][j] != EMPTY:
        raise InvalidActionError(action, board, 'Result function tried to perform invalid action on occupaied tile: ')

    # Make a deep copy of the board and update with the current player's move:
    board_copy = copy.deepcopy(board)
    board_copy[i][j] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # # If Winning way with row
    for rowWin in board:
        if rowWin.count(O) == 3:
            return O
        if rowWin.count(X) == 3:
            return X
    # # If Winning way with column
    # for columns in range(3):
    #     column =''
    #     for everyCell in range(3):
    #         column=column+str(board[everyCell][columns])
    #
    # if column=='OOO':
    #     return O
    # if column=='XXX':
    #     return X
    # # If Winning way with cross
    # cross1 =''
    # cross2 =''
    # numberOfCrosses=2
    # for row in range(3):
    #     cross1 = cross1+str(board[row][row])
    #     cross2 =cross2+ str(board[row][numberOfCrosses])
    #     numberOfCrosses= numberOfCrosses-1
    #
    # if cross1 == 'OOO' or cross2 == 'OOO':
    #     return O
    # elif cross1 == 'XXX' or cross2 == 'XXX':
    #     return X
    #
    # #If there is no Winner
    # return None

    for j in range(3):
        column = ''
        for i in range(3):
            column += str(board[i][j])

        if column == 'XXX':
            return X
        if column == 'OOO':
            return O

        # Check Diagonals:
    diag1 = ''
    diag2 = ''
    j = 2

    for i in range(3):
        diag1 += str(board[i][i])
        diag2 += str(board[i][j])
        j -= 1

    if diag1 == 'XXX' or diag2 == 'XXX':
        return X
    elif diag1 == 'OOO' or diag2 == 'OOO':
        return O

    # Otherwise no current winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global actions_explored, currentGreatestUtility
    actions_explored = 0

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            successor = result(board, action)
            v = max(v, min_value(successor))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            successor = result(board, action)
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        currentGreatestUtility = -math.inf
        for action in actions(board):
            successor = result(board, action)
            pathMaximumUtility = min_value(successor)
            if pathMaximumUtility > currentGreatestUtility:
                currentGreatestUtility = pathMaximumUtility  # Assigns the largest achievable utility from this board subtree
                best_move = action  # Assigns the action that'll lead you to the largest utility node
    else:
        currentLeastUtility = math.inf
        for action in actions(board):
            successor = result(board, action)
            pathMinimumUtility = max_value(successor)
            if pathMinimumUtility < currentLeastUtility:  # If this path has a
                currentLeastUtility = pathMinimumUtility  # Assigns the least achievable utility from this board subtree
                best_move = action  # Assigns the action that'll lead you to the least utility node
    return best_move
