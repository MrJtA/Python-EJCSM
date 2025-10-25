"""
32. Modificar el ejercicio anterior para que trabaje con la baraja española. Esta consta de
40 cartas: 2, 3, 4, 5, 6, 7, sota, caballo, rey y as.
"""

import random

def Ejercicio32():
    listaPalos = ["oros", "copas", "espadas", "bastos"]
    listaNumeros = ["as", 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"]
    palo = random.randint(0, len(listaPalos)-1)
    numero = random.randint(0, len(listaNumeros)-1)
    print(f"{listaNumeros[numero]} de {listaPalos[palo]}")

Ejercicio32()