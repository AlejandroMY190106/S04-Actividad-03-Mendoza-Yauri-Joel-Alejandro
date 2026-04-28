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
    """
    Returns player who has the next turn on a board.
    """
    ##Contar cuantas X y cuantas O hay
    cantidad_X = 0
    cantidad_O = 0
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):
            if board[i][j] == X:
                cantidad_X += 1
            if board[i][j] == O:
                cantidad_O += 1
    if cantidad_X > cantidad_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):    
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Crear una copia profunda del tablero para no mutar el original
    tablero_nuevo = [fila.copy() for fila in board]
    if tablero_nuevo[i][j] != EMPTY:
        raise Exception("Accion Invalida")
    tablero_nuevo[i][j] = player(board)
    return tablero_nuevo


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Revisar filas
    for fila in board:
        if fila[0] == fila[1] == fila[2] and fila[0] is not None:
            return fila[0]
    # Revisar columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    # Revisar diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
  
    ##Revisar si el tablero está lleno
    for i, fila in enumerate(board):
        for j, valor in enumerate(fila):    
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def maximo_valor(b):
        if terminal(b):
            return utility(b)
        v = -math.inf
        for a in actions(b):
            v = max(v, minimo_valor(result(b, a)))
        return v

    def minimo_valor(b):
        if terminal(b):
            return utility(b)
        v = math.inf
        for a in actions(b):
            v = min(v, maximo_valor(result(b, a)))
        return v

    actual = player(board)
    movimiento = None

    if actual == X:
        mejor_valor = -math.inf
        for action in actions(board):
            valor = minimo_valor(result(board, action))
            if valor > mejor_valor:
                mejor_valor = valor
                movimiento = action
    else:
        mejor_valor = math.inf
        for action in actions(board):
            valor = maximo_valor(result(board, action))
            if valor < mejor_valor:
                mejor_valor = valor
                movimiento = action

    return movimiento