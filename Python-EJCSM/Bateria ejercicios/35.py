"""
35. Diseña una aplicación que muestre las tablas de multiplicar del 1 al 10.
"""

def Ejercicio35():
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")
        print()

Ejercicio35()