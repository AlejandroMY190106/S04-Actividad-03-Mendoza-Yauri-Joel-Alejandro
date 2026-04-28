"""
Tic Tac Toe Player
"""

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
    count_x = 0
    count_o = 0
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if board[i][j] == X:
                count_x = count_x + 1
            if board[i][j] == O:
                count_o = count_o + 1
    if count_x == count_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    casillas_vacias = set()
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if valor == EMPTY:
                casillas_vacias.add((i,j))
    return casillas_vacias

import copy
def result(board, action):
    if action not in actions(board):
        raise Exception("Movimiento ilegal")
    i, j = action
    ficha = player(board)
    nuevo = copy.deepcopy(board)
    nuevo[i][j] = ficha
    return nuevo



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


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
