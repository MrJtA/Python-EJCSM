"""
25. Muestra 20 números enteros aleatorios entre 0 y 10 (ambos incluidos) separados por
espacios.
"""

import random

def Ejercicio25():
    print("Los 20 números aleatorios generados entre el 0 y 10 son: ", end="")
    for i in range(1, 21):
        x = random.randint(0, 10)
        print(x, end=" ")
    print("\n")

Ejercicio25()