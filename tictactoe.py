"""
Tic Tac Toe Player
"""
import copy
import math
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
    numberOfMoves = 0
    numberOfEmptyCells = 0
    for i in range(3):
        for j in range(3):
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
    for i in range(3):
        for j in range(3):
            if (board[i][j] == EMPTY):
                setOfPossibleMoves.append((i,j))
    return setOfPossibleMoves


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
    # If Winning way with row
    for rowWin in board:
        if rowWin.count(O) == 3:
            return O
        if rowWin.count(X) == 3:
            return X
    # If Winning way with column
    for columns in range(3):
        column =""
        for everyCell in range(3):
            column=column+str(board[everyCell][columns])
        if column=="OOO":
            return O
        if column=="XXX":
            return X
        # If Winning way with cross
    cross1 =''
    cross2 =''
    numberOfCrosses=0
    for row in range(3):
        cross1 = cross1+str(board[row][numberOfCrosses])
        cross2 =cross2+ str(board[row][row])
        numberOfCrosses= numberOfCrosses+1

    if cross1 == 'OOO' or cross2 == 'OOO':
        return O
    if cross1 == 'XXX' or cross2 == 'XXX':
        return X

    #If there is no Winner
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=False:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) =='X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    global actions_explored
    actions_explored = 0

    def max_player(board, best_min=10):
        """ Helper function to maximise score for 'X' player.
            Uses alpha-beta pruning to reduce the state space explored.
            best_min is the best result
        """

        global actions_explored

        # If the game is over, return board value
        if terminal(board):
            return (utility(board), None)

        # Else pick the action giving the max value when min_player plays optimally
        value = -10
        best_action = None

        # Get set of actions and then select a random one until list is empty:
        action_set = actions(board)

        while len(action_set) > 0:
            action = random.choice(tuple(action_set))
            action_set.remove(action)

            # A-B Pruning skips calls to min_player if lower result already found:
            if best_min <= value:
                break

            actions_explored += 1
            min_player_result = min_player(result(board, action), value)
            if min_player_result[0] > value:
                best_action = action
                value = min_player_result[0]

        return (value, best_action)

    def min_player(board, best_max=-10):
        """ Helper function to minimise score for 'O' player """

        global actions_explored

        # If the game is over, return board value
        if terminal(board):
            return (utility(board), None)

        # Else pick the action giving the min value when max_player plays optimally
        value = 10
        best_action = None

        # Get set of actions and then select a random one until list is empty:
        action_set = actions(board)
        print(actions(board))
        while len(action_set) > 0:
            action = random.choice(tuple(action_set))
            action_set.remove(action)

            # A-B Pruning skips calls to max_player if higher result already found:
            if best_max >= value:
                break

            actions_explored += 1
            max_player_result = max_player(result(board, action), value)
            if max_player_result[0] < value:
                best_action = action
                value = max_player_result[0]

        return (value, best_action)

    # If the board is terminal, return None:
    if terminal(board):
        return None

    if player(board) == 'X':
        print('AI is exploring possible actions...')
        best_move = max_player(board)[1]
        print('Actions explored by AI: ', actions_explored)
        return best_move
    else:
        print('AI is exploring possible actions...')
        best_move = min_player(board)[1]
        print('Actions explored by AI: ', actions_explored)
        return best_move