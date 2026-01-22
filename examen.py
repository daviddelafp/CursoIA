def bloque_valido(numeros):
    vistos = [False, False, False, False, False, False, False, False, False]  # lista de 9 para comprobrar si han salido en la lista

    i = 0
    while i < 9:
        v = numeros[i]
        if v < 1 or v > 9: #comprobar que los numeros estén entre 1 y 9
            return False

        indice = v - 1 #cambiar el indice para ir de 1-9 y no de 0-8
        if vistos[indice]:
            return False #si un numero está visto se devuelve false
        vistos[indice] = True #si el numero no está en visto true

        i += 1

    return True


def sudoku_valido(tablero):     # Comprobar que el tamaño es 9x9

    if len(tablero) != 9:
        return False

    i = 0
    while i < 9:
        if len(tablero[i]) != 9:
            return False
        i += 1

    # Verificar filas
    fila = 0
    while fila < 9:
        if not bloque_valido(tablero[fila]):
            return False
        fila += 1

    # Verificar columnas
    col = 0
    while col < 9:
        columna = []
        fila = 0
        while fila < 9:
            columna.append(tablero[fila][col])
            fila += 1
        if not bloque_valido(columna):
            return False
        col += 1

    # Verificar subcuadrículas 3x3
    inicio_fila = 0
    while inicio_fila < 9:
        inicio_col = 0
        while inicio_col < 9:
            bloque = []
            f = inicio_fila
            while f < inicio_fila + 3:
                c = inicio_col
                while c < inicio_col + 3:
                    bloque.append(tablero[f][c])
                    c += 1
                f += 1

            if not bloque_valido(bloque):
                return False

            inicio_col += 3
        inicio_fila += 3

    return True

tablero = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

print(sudoku_valido(tablero))  # True















x=5
y=2

print(x//y)