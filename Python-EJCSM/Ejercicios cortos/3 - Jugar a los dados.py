"""
Vamos a realizar un juego de dados, en dicho juego van a participar un jugador y la banca.
El jugador tira dos dados (la numeración de cada uno es del 1 al 6).
En cada tirada puede pasar lo siguiente:
• El jugador gana si la suma de los puntos es 7 u 11.
• El jugador pierde si la suma de los puntos son 2, 3, 10 ó 12.
• En cualquier otro caso se repite la tirada
Realiza el programa que simula el juego de principio a fin.
"""

import random

ganadores = [7, 11]
perdedores = [2, 3, 10, 12]

while True:
    print("¿Quieres tirar un dado?")
    opcion = int(input("1. Sí.\n2. No.\n"))
    match opcion:
        case 1:
            while True:
                dado1 = random.randint(1, 6)
                dado2 = random.randint(1, 6)
                print("El primer dado ha dado", dado1)
                print("El segundo dado ha dado", dado2)
                suma = dado1 + dado2
                if suma in ganadores:
                    print("Has ganado.")
                    break
                elif suma in perdedores:
                    print("Has perdido.")
                    break
                else:
                    print("Se tirará otro dado.")
                    continue
        case 2:
            print("Hasta la próxima.")
            break
        case _: continue