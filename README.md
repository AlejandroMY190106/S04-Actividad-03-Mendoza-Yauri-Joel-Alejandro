Tic Tac Toe - Solucion en tictactoe.py

Este repositorio incluye una implementacion del agente para el juego Tic Tac Toe (Tres en raya).
El archivo principal de la actividad es tictactoe.py, donde se resuelve la logica del juego y
el algoritmo de decision.

Objetivo

Implementar un agente que elija el movimiento optimo usando Minimax, con estas piezas clave:

- representacion del tablero
- reglas del juego (ganador, terminal, utilidad)
- generacion de acciones validas
- busqueda Minimax para elegir la mejor jugada

Contenido de tictactoe.py

Constantes y estado inicial

- X, O, EMPTY: representan los jugadores y casillas vacias
- initial_state(): crea un tablero 3x3 con None

Turnos y acciones

- player(board): determina el jugador que mueve segun la cantidad de X y O
- actions(board): retorna el conjunto de posiciones (i, j) disponibles
- result(board, action): devuelve un nuevo tablero con la jugada aplicada

Reglas del juego

- winner(board): detecta ganador en filas, columnas o diagonales
- terminal(board): indica si el juego termino (ganador o tablero lleno)
- utility(board): retorna 1 si gana X, -1 si gana O, 0 en empate

Algoritmo Minimax

- minimax(board): calcula el movimiento optimo para el jugador actual
- maximo_valor / minimo_valor: evaluan recursivamente el valor de cada accion

Representacion del tablero

El tablero es una lista de listas de 3x3 con valores:

- "X" para jugador X
- "O" para jugador O
- None para casillas vacias

Uso rapido

Ejemplo de uso desde otro modulo:

```python
from tictactoe import initial_state, minimax, result

board = initial_state()
best_move = minimax(board)
board = result(board, best_move)
```

Notas

- result(board, action) crea una copia del tablero para evitar mutaciones.
- minimax devuelve None si el estado es terminal.
