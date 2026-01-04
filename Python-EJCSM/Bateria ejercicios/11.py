"""
11. Modifica el ejercicio anterior para que en vez de mostrar *, muestre números
naturales correlativos; ejemplo:
1
1 2
1 2 3
"""

def Ejercicio11():
    N = int(input("N: "))
    for i in range(1, N+1):
        print()
        for j in range(1, i+1):
            print(j, end=" ")

Ejercicio11()