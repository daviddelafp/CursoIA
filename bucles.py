#Bucles
'''
#Bucle for básico
for i in range(5):
       print(i)
'''


'''
#Bucle while básico
x=0
while x<10:
        print("Hola Mundo")
        x=x+1
'''


'''
# Bucle dentro de una funcion
def imprimeX(x):
    i=0
    while i<x:
        print("hola")
        i+=1

imprimeX(11)
'''


'''
#Lista
cuadrados=[]
i=0
while i<5:
    cuadrados.append(i**2)
    print(cuadrados)
    i+=1 
'''

'''
#try except
x=input("dame tu numero: ")
try:
    print(100/int(x))
except:
    print("error")
'''

'''
#Creación de ficheros w(crea el fichero si no existe
#f=open("datos.txt","w")
f=open("datos.txt")
#f.write("Hola python 1")
contenido=f.read()
print(contenido)
f.close()
'''

'''
#quitar espacios de un txt
f=open("datos.txt")
for i in f:
    print(i.strip())
f.close
'''


'''
#recibe un vector como parametro y que devueva el valor maximo que tenga esa lista
def maximo(vector):
    print(max(vector))

maximo([1,2,3,4,5,6,7])
'''