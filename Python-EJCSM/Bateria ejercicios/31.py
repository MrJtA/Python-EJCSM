"""
31. Realiza un programa que muestre al azar el nombre de una carta de la baraja francesa
(cuatro palos: picas, corazones, diamantes y tréboles. Cada palo está formado por 13
cartas, de las cuales 9 cartas son numerales y 4 literales: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q,
K y A que sería el 1).
"""

import random

def Ejercicio31():
    listaPalos = ["picas", "corazones", "diamantes", "tréboles"]
    listaNumeros = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    palo = random.randint(0, len(listaPalos)-1)
    numero = random.randint(0, len(listaNumeros)-1)
    print(f"{listaNumeros[numero]} de {listaPalos[palo]}")

Ejercicio31()