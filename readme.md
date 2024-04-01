Juego del Gato (Tic Tac Toe)
============================

Este es un juego de Gato (Tic Tac Toe) implementado en Python. Puedes jugar contra otro jugador, contra la máquina (versión aleatoria) o contra la máquina que utiliza el algoritmo Minimax para tomar decisiones estratégicas.

Instrucciones de juego
----------------------

1.  Ejecuta el script `main.py`.
2.  Selecciona una opción:
    *   **Jugador contra jugador:** Dos jugadores se turnan para marcar el tablero.
    *   **Jugador contra Máquina (Aleatorio):** Un jugador humano juega contra la máquina, que elige sus movimientos de forma aleatoria.
    *   **Jugador contra Máquina (Minimax):** Un jugador humano juega contra la máquina, que utiliza el algoritmo Minimax para tomar decisiones estratégicas.
3.  Sigue las instrucciones en pantalla para seleccionar una casilla para realizar tu movimiento. (selecciona casillas con los números 0-9)
4.  El juego continúa hasta que uno de los jugadores gane o se produzca un empate.

Cómo funciona
-------------

*   La función `print_board` muestra el tablero actual en la consola.
*   La función `verify_player` verifica si un jugador ha ganado el juego.
*   La función `empty_squares` devuelve una lista de casillas vacías en el tablero.
*   El algoritmo Minimax se implementa en la función `minimax`, que determina el mejor movimiento posible para la máquina.
*   La función `cpu_move` elige el mejor movimiento posible para la máquina utilizando el algoritmo Minimax.
*   La función `jugar_gato` controla el flujo del juego y permite a los jugadores realizar movimientos.
