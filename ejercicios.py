#coleccion de ejercicios


#EJERCICIO 1 JUEGO DE SUMAS
def ejercicio1():
 import random
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
 import random
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

def ejercicio3()
    import random
    bucle=true
    positivos=0
    negativos=0
    while bucle:
        dato=input("Introduce un número : ")
        if dato>0:
            positivos+=1
        else if dato<0:
            negativos+=1
        else
            bucle=false
            
ejercicio3()