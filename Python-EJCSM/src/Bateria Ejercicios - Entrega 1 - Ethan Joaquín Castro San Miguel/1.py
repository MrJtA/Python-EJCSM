"""
1. Hacer un programa en el que se pida por teclado un número mayor que 2 (el programa
controlará que cumpla esto), y lo imprima de todas las formas posibles como producto
de dos factores (no se tiene en cuenta la multiplicación por 1). Por ejemplo: Con el
número 36, tendría que visualizarse: 18*2, 12*3, 9*4, 6*6, 3*12, 4*9, 2*18.
"""
def Ejercicio1():
    n = 0
    while n<=2:
        n = int(input("Introduce un número: "))
        for i in range (2, n):
            if n%i == 0:
                print(int((n/i)),"*",i,", ",end='')

Ejercicio1()