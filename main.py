import random

def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        print("-" * 5)

def verify_player(board, player):
    # Verificar filas
    for i in range(0, 9, 3):
        if all(square == player for square in board[i:i+3]):
            return True
    # Verificar columnas
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Verificar diagonales
    if all(board[i] == player for i in range(0, 9, 4)) or all(board[i] == player for i in range(2, 7, 2)):
        return True
    return False

def empty_squares(board):
    return [i for i in range(9) if board[i] == " "]

def minimax(board, maximizing_player, depth=0):
    if verify_player(board, "X"):
        return -10 + depth
    elif verify_player(board, "O"):
        return 10 - depth
    elif " " not in board:
        return 0

    if maximizing_player:
        best_score = float("-inf")
        for square in empty_squares(board):
            board[square] = "O"
            score = minimax(board, False, depth + 1)
            board[square] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for square in empty_squares(board):
            board[square] = "X"
            score = minimax(board, True, depth + 1)  # Incrementamos la profundidad aquí
            board[square] = " "
            best_score = min(score, best_score)
        return best_score

def cpu_move(board):
    best_score = float("-inf")
    best_move = None  # Inicializamos best_move
    for square in empty_squares(board):
        board[square] = "O"
        score = minimax(board, False)
        board[square] = " "
        if score > best_score:
            best_score = score
            best_move = square
    return best_move

def jugar_gato():
    print("Bienvenido al juego del Gato!")
    print("Seleccione una opción:")
    print("1. Jugador contra jugador")
    print("2. Jugador contra Máquina (Aleatorio)")
    print("3. Jugador contra Máquina (Minimax)")

    option = input("Opción: ")

    if option == "1":
        current_player = "X"
    elif option == "2":
        current_player = "X"
    elif option == "3":
        current_player = "X"
    else:
        print("Opción no válida.")
        return

    board = [" "]*9

    while True:
        print_board(board)
        
        # Verificar el estado del juego después de cada turno
        if verify_player(board, "X"):
            print("¡El jugador X ha ganado!")
            break
        elif verify_player(board, "O"):
            print("¡El jugador O ha ganado!")
            break
        elif " " not in board:
            print("¡Empate!")
            break

        if option == "1" or current_player == "X":
            move = int(input(f"Jugador {current_player}, elige un número del 0 al 8: "))
        elif option == "2":
            move = random.choice(empty_squares(board))
            print(f"La máquina ha elegido la casilla {move}")
        elif option == "3":
            move = cpu_move(board)
            print(f"La máquina ha elegido la casilla {move}")

        if 0 <= move <= 8 and board[move] == " ":
            board[move] = current_player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Movimiento inválido, por favor elige un número válido y una casilla vacía.")

if __name__ == "__main__":
    jugar_gato()
