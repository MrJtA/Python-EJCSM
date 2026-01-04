"""
Realiza el método que reciba una longitud, un máximo y un mínimo y devuelva una lista
numérica rellenada de forma aleatoria con números comprendidos entre ese máximo y
mínimo y con esa longitud.
"""

import random

def crearLista(a : int, b : int, c: int) -> list[int]:
    lista = []
    for i in range(0, c):
        n = random.randint(a, b)
        lista.append(n)
    return lista

maximo = int(input("Introduce el máximo: "))
minimo = int(input("Introduce el mínimo: "))
longitud = int(input("Introduce la longitud: "))

print(crearLista(maximo, minimo, longitud))