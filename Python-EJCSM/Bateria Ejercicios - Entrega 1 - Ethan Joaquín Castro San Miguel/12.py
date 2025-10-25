"""
12. Haz un programa para imprimir una tabla de tres columnas y N filas con los cuadrados
y los cubos de los N primeros números. Pide N al usuario.
"""

def Ejercicio12():
    N = int(input("N: "))
    for i in range(1, N+1):
        print()
        for j in range(1, 4):
            print(i**j, end=" ")

Ejercicio12()