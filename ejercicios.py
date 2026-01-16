#coleccion de ejercicios
import random
import os
##NIVEL 1 FUNDAMENTOS##

#EJERCICIO 1 JUEGO DE SUMAS
def ejercicio1():

 x=random.randint(10,99)
 y=random.randint(10,99)
 print(x+y)
 dato=input("Suma estos dos números: " + str(x) + " y " + str(y) + " = \n")

 if int(dato)==(x+y):
     print("La suma es correcta")
 else:
     print("La suma es incorrecta")


#ejercicio1()


#EJERCICIO 2 JUEGO DE SUMAS REPETIDAS
def ejercicio2():

 contador=0
 for i in range(5):
        
        x=random.randint(10,99)
        y=random.randint(10,99)
        print(x+y)
        dato=input("Suma estos dos números: " + str(x) + " y " + str(y) + " = \n")

        if int(dato)==(x+y):
            contador+=1
 print("Has acertado " + str(contador) + " sumas")       

#ejercicio2()



#EJERCICIO 3 CONTADOR DE POSITIVOS Y NEGATIVOS
def ejercicio3():

    bucle=True
    positivos=0
    negativos=0
    while bucle:
        try:
            dato=input("Introduce un número : ")
            if int(dato)>0:
                positivos+=1
            elif int(dato)<0:
                negativos+=1
            else:
                bucle=False
        except:
            print("El dato introducido no es un numero, error")

    print("Hay " + str(positivos) + " numeros positivos y " + str(negativos) + " numeros negativos.") 

#ejercicio3()



##NIVEL 2 LISTAS Y CONTROL DE FLUJO##


#EJERCICIO 4 ESTADISTICA BASICA
def ejercicio4():
    
    a = []
    for i in range(20):
        
        a.append(random.randint(1,100))
    

    print("Numero maximo:" + max(a)) #Numero maximo
    print("Numero minimo:" + min(a)) #Numero minimo

    # Media de la lista
    media = sum(a) / len(a)

    # Contar números pares
    pares = sum(1 for n in a if n % 2 == 0)

    print("La media de la lista es:" + media)
    print("Hay" + pares + "numeros pares en la lista")


#ejercicio4()


#EJERCICIO 5 ELIMINAR DUPLICADOS
def ejercicio5():
    a = []
    b = []
    for i in range(20):
        
        a.append(random.randint(1,10))
    
    print("Lista original: " + str(a))

    for elemento in a:
        if elemento not in b:
            b.append(elemento)
    
    print("Lista sin duplicados: " + str(b))


#ejercicio5()


#NIVEL 3 STRINGS Y FICHEROS

#EJERCICIO 6 CONTADOR DE PALABRAS
def ejercicio6():
    try:
         f=open("datos.txt","r")
         lineas = f.readlines()
    except FileNotFoundError:
        print("No se encontró el fichero datos.txt")
        return

    num_lineas = len(lineas)
    num_palabras = sum(len(line.split()) for line in lineas)

    print("El fichero tiene " + str(num_lineas) + " lineas y " + str(num_palabras) + " palabras.")

#ejercicio6()

'''
#EJERCICIO 7: leer datos.txt y contar lineas y palabras
def ejercicio7():
    try:
         f=open("quijote.txt","r")
         lineas = f.readlines()
    except FileNotFoundError:
        print("No se encontró el fichero datos.txt")
        return

    num_lineas = len(lineas)
    num_palabras = sum(len(line.split()) for line in lineas)

    print("El fichero tiene " + str(num_lineas) + " lineas y " + str(num_palabras) + " palabras.")


ejercicio7()
'''

def ejercicio10(matriz):

    filas = len(matriz)
    columnas = len(matriz[0])

    if matriz[0][0] == 1:
        return False

    matrizComprobar = [[False] * columnas for _ in range(filas)]
    matrizComprobar[0][0] = True

    # Primera fila
    for j in range(1, columnas):
        if matriz[0][j] == 0 and matrizComprobar[0][j-1]:
            matrizComprobar[0][j] = True

    # Primera columna
    for i in range(1, filas):
        if matriz[i][0] == 0 and matrizComprobar[i-1][0]:
            matrizComprobar[i][0] = True

    # Resto
    for i in range(1, filas):
        for j in range(1, columnas):
            if matriz[i][j] == 0 and (matrizComprobar[i-1][j] or matrizComprobar[i][j-1]):
                matrizComprobar[i][j] = True

    return matrizComprobar[filas-1][columnas-1]



matriz = [
    [0,0,0,1,0,0,0,0,0,0],
    [1,1,0,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,0,1,1,0,1,0],
    [0,1,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,0,1,0,1,0],
    [0,1,0,1,0,0,0,0,1,0],
    [0,1,0,1,0,1,1,0,1,0],
    [0,0,0,1,0,0,0,0,0,0],
    [1,1,0,0,0,1,1,1,1,0],
]


if ejercicio10(matriz):
    print("✅ Sí existe un camino desde la esquina superior izquierda hasta la inferior derecha.")
else:
    print("❌ No existe camino desde la esquina superior izquierda hasta la inferior derecha.")





