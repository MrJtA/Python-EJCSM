"""
10. Hacer un programa que lea por teclado un numero N e imprima un triángulo
rectángulo, de N filas. EJ: N=5, se pintará lo siguiente:
*
* *
* * *
* * * *
* * * * *
"""

def Ejercicio10():
    N = int(input("N: "))
    cadena = ""
    for i in range(1, N+1):
        cadena = cadena+"*"
        print(cadena)

Ejercicio10()