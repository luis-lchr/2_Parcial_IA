def imprimir_tablero(tablero):
    print("  0   1   2")
    for i, row in enumerate(tablero):
        print(i, end=" ")
        for cell in row:
            print(f" {cell} ", end="")
            if cell != " ":
                print("|", end="")
            else:
                print(" ", end="")
        print("\n  ---|---|---")

# Función para verificar si alguien ya ganó
def checar_ganador(tablero, jugador):
    for row in tablero:
        if all([cell == jugador for cell in row]):
            return True

    for col in range(3):
        if all([tablero[row][col] == jugador for row in range(3)]):
            return True

    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

# Función para verificar si hay empate
def checar_empate(tablero):
    return all(cell != " " for row in tablero for cell in row)

# Función para generar movimientos válidos
def mov_validos(tablero):
    return [(row, col) for row in range(3) for col in range(3) if tablero[row][col] == " "]

# Función que implementa el algoritmo Minimax
def minimax(tablero, jugador):
    if checar_ganador(tablero, "X"):
        return -1
    if checar_ganador(tablero, "O"):
        return 1
    if checar_empate(tablero):
        return 0

    if jugador == "O":
        best_score = float("-inf")
        for move in mov_validos(tablero):
            tablero[move[0]][move[1]] = "O"
            score = minimax(tablero, "X")
            tablero[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in mov_validos(tablero):
            tablero[move[0]][move[1]] = "X"
            score = minimax(tablero, "O")
            tablero[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

# Función para que la computadora haga su movimiento usando Minimax
def mov_compu(tablero):
    best_score = float("-inf")
    best_move = None
    for move in mov_validos(tablero):
        tablero[move[0]][move[1]] = "O"
        score = minimax(tablero, "X")
        tablero[move[0]][move[1]] = " "
        if score > best_score:
            best_score = score
            best_move = move
    tablero[best_move[0]][best_move[1]] = "O"

# Función principal para jugar al gato
def main():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    print("¡Vamos a jugar al gato!")

    while True:
        imprimir_tablero(tablero)
        print("\n")
        if jugador == "X":
            row, col = map(int, input("Ingresa tu jugada (fila y columna ej: 0 1): ").split())
            
            if tablero[row][col] == " ":
                tablero[row][col] = "X"
            else:
                print("Casilla ocupada. Inténtalo de nuevo.")
                continue
        else:
            mov_compu(tablero)

        if checar_ganador(tablero, jugador):
            imprimir_tablero(tablero)
            print(f"{jugador} ha ganado")
            break
        elif checar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
        jugador = "X" if jugador == "O" else "O"

if __name__ == "__main__":
    main()