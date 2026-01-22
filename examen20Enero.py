import math
def ejercicio4(lista): #escribir una función que reciba una lista de numeros y devuelva la media
    
    suma = 0  #definir variable para sumar todos los números de la lista
    i = 0     #variable para recorrer el bucle

                             #versión con librerias
    suma = math.fsum(lista)  #en la variable suma mete el sumatorio de lista
    return suma / len(lista) #divide lista entre el tamaño de la lista

    while i < len(lista):   #bucle que recorre la lista por su tamaño
        suma += lista[i]    #suma todos los números de una lista en la variable
        i += 1              #suma un numero para que el bucle recorra la lista

    return suma / len(lista)    #devuelve la suma dividido entre el numero de numeros en la lista

lista=[1,2,3,4,5,6,7,99,999]       #se crea una lista para pasársela a la función
#print(ejercicio4(lista))  #con los números que hay la media es4


def ejercicio5(texto): #dada una cadena de texto, devuelve un diccionario con la frecuencia de cada caracter

    frecuencia = {}    #crear un diccionario para guardar las repeticiones de los caracteres
    i = 0              #variable para recorrer el bucle(texto)
    while i < len(texto):     #bucle para recorrer el texto en base a su tamaño
        c = texto[i]          #variable para guardar el texto en una lista
        if c in frecuencia:   #si letra está en la lista
            frecuencia[c] += 1  #sumar uno a la lista
        else:                   #si no 
            frecuencia[c] = 1   #la freuencia es 1 por lo tanto lo escribes en la lista
        i += 1              #pasar a la siguiente letra del texto
    return frecuencia 

#print(ejercicio5("holaaaaaaaa"))


def ejercicio7(lista):   #comprobar si un alista está ordenada de forma ascendente
    
    i = 0                              #variable para recorrer la lista con el bucle
    while i < len(lista) - 1:          #bucle para recorrer la lista en base a su tamaño -1 porque en la ultima iteración ya estaría fuera del bucle
        if lista[i] > lista[i + 1]:    #comprueba si el numero actual es menor que el siguiente del bucle
            return False               #return false
        i += 1      
    return True


lista=[1,2,3]
#print(ejercicio7(lista))


def ejercicio8_verificarbloque(numeros):
    numerosVistos=[False,False,False,False,False,False,False,False,False]
 
    i = 0                  #variable para recorrer el bucle
    while i < 9:           #bucle que se recorrerá 9 veces
        v = numeros[i]     #variable para recorrer los numeros de la lista 1 por 1
        if v < 1 or v > 9: #comprobar que los numeros estén entre 1 y 9
            return False   #si los numeros no están entre 1 y 9 False

        indice = v - 1 #cambiar el indice para ir de 1-9 y no de 0-8
        if numerosVistos[indice]: #si 
            return False #si un numero está visto se devuelve false

        numerosVistos[indice] = True #si el numero no está en visto true

        i += 1

    return True


def ejercicio8(tablero):    #verificación sudoku

    fila = 0                #definir filas
    while fila < 9:         #bucle para recorrer las filas
        if not ejercicio8_verificarbloque(tablero[fila]):   #llamar al verificador y le pasas la fila
            return False   #si no vuelve true devolver false
        fila += 1

    
    col = 0                 #definir las columnas
    while col < 9:          #bucle para recorrer las columnas 
        columna = []        #crear una lista para meter la columna
        fila = 0            #variable para recorrer las filas
        while fila < 9:     #recorrer la fila
            columna.append(tablero[fila][col])  #añadir a columna el valor de la fila
            fila += 1
        if not ejercicio8_verificarbloque(columna): #comprobar si la columna no devuelve true
            return False                            #si entra aqui devolver falso
        col += 1                                    #comprobar la siguiente columna

    inicio_fila = 0                     #indicas que la primera fila es 0,3,9 despues del +3 de abajo
    while inicio_fila < 9:              #se recorre la fila
        inicio_col = 0                  #indicas que la primera columna es 0,3,9 despues del +3 de abajo
        while inicio_col < 9:           #se recorre la columna
            bloque = []                 #creo un bloque para guardar el dato del 3x3
            f = inicio_fila             #guardas el valor del 0,3,9 del bloque
            while f < inicio_fila + 3:  #recorrer las 3 filas del bloque
                c = inicio_col          #
                while c < inicio_col + 3:  #recorrer las 3 columnas del bloque
                    bloque.append(tablero[f][c]) # se añade cada fila del bucle al tablero
                    c += 1              #siguiente columna dentro del bloque
                f += 1                  #siguiente fila dentro del bloque

            if not ejercicio8_verificarbloque(bloque):   #verificar si el bloque es o no valido
                return False                #devolver falso

            inicio_col += 3             #sumas el inicio de la columna +3 para empezar el siguiente grupo
        inicio_fila += 3                #sumas el inicio de la fila +3 para empezar el siguiente grupo



    return True         #si todas las comprobaciones anteriores son correctas devolver True

tablero = [
    [5,3,4,6,7,8,9,1,33],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
print(ejercicio8(tablero))  # True