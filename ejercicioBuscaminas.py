# generar_mapa_buscaminas.py
# Uso: python generar_mapa_buscaminas.py <filas> <columnas> <numero_minas>

import sys
import random

def imprimir_error_y_salir():
    # Mensaje simple (puedes ajustarlo si tu profe quiere uno concreto)
    print("Error: parámetros inválidos.")
    sys.exit(1)

def contar_minas_adyacentes(tablero, f, c, filas, columnas):
    contador = 0
    df = -1
    while df <= 1:
        dc = -1
        while dc <= 1:
            if not (df == 0 and dc == 0):
                nf = f + df
                nc = c + dc
                if nf >= 0 and nf < filas and nc >= 0 and nc < columnas:
                    if tablero[nf][nc] == 'X':
                        contador += 1
            dc += 1
        df += 1
    return contador

def main():
    # 1) Comprobar número de parámetros
    if len(sys.argv) != 4:
        imprimir_error_y_salir()

    filas_s = sys.argv[1]
    columnas_s = sys.argv[2]
    minas_s = sys.argv[3]

    # 2) Validar que son enteros usando isdigit()
    if not filas_s.isdigit() or not columnas_s.isdigit() or not minas_s.isdigit():
        imprimir_error_y_salir()

    filas = int(filas_s)
    columnas = int(columnas_s)
    numero_minas = int(minas_s)

    # 3) Validar que son > 0
    if filas <= 0 or columnas <= 0 or numero_minas <= 0:
        imprimir_error_y_salir()

    # 4) Validar que minas <= filas*columnas
    total_casillas = filas * columnas
    if numero_minas > total_casillas:
        imprimir_error_y_salir()

    # 5) Semilla fija para que sea reproducible
    random.seed(0)

    # 6) Crear tablero inicial (todo '0' de momento)
    tablero = []
    f = 0
    while f < filas:
        fila = []
        c = 0
        while c < columnas:
            fila.append('0')
            c += 1
        tablero.append(fila)
        f += 1

    # 7) Colocar minas aleatoriamente sin sobreescribir
    colocadas = 0
    while colocadas < numero_minas:
        rf = random.randrange(filas)
        rc = random.randrange(columnas)

        if tablero[rf][rc] != 'X':
            tablero[rf][rc] = 'X'
            colocadas += 1

    # 8) Calcular números en casillas que no son mina
    f = 0
    while f < filas:
        c = 0
        while c < columnas:
            if tablero[f][c] != 'X':
                n = contar_minas_adyacentes(tablero, f, c, filas, columnas)
                tablero[f][c] = str(n)
            c += 1
        f += 1

    # 9) Imprimir tablero final (cada fila en una línea, sin espacios)
    f = 0
    while f < filas:
        linea = ""
        c = 0
        while c < columnas:
            linea += tablero[f][c]
            c += 1
        print(linea)
        f += 1

if __name__ == "__main__":
    main()