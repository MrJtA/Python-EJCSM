"""
7 y medio.

Vamos a replicar el juego de cartas 7 y medio, pero para un solo jugador.
Para el juego se usa una baraja española de 40 cartas.
(1, 2, 3, 4, 5, 6, 7, Sota, Caballo, Rey),
	de 4 palos (oros, bastos, copas y espadas)

Como para este juego dan igual los palos, simplemente cada valor estará 4 veces en nuestra baraja.

El juego consiste en sumar 7 puntos y medio o menos.
Cada carta suma a tu puntuación su valor numérico, excepto la Sota, el Caballo y el Rey, que suman 0.5.

El juego inicia repartiéndote una carta y preguntándote si quieres plantarte o pedir otra.

Si te plantas el juego se acaba y mostrará tu puntuación total.
Si pides otra carta se actualizará tu puntuación, y en caso de que esta sea 7,5 o menos, volverá a preguntarte.
Si tus puntos son de 8 o más, automáticamente has perdido, el programa te informará, y se cerrará.
"""

import random
from string import punctuation

valores = (1, 2, 3, 4, 5, 6, 7, "Sota", "Caballo", "Rey")
palos = ("Espadas", "Bastos", "Oros", "Bastos")
baraja = []

for valor in valores:
    for palo in palos:
        carta = (valor, palo)
        baraja.append(carta)

def pedirCarta():
    dupla = random.choice(baraja)
    c = dupla[0]
    print(f"Carta recibida: {dupla}")
    if isinstance(c, str):
        punctuation = 0.5
    else:
        punctuation = c

def Ejercicio():
    dupla = random.choice(baraja)
    print("Se ha sacado una carta aleatoria. Tienes que adivinar el palo: ")
    contador = 0
    d = ""
    while d != dupla[1]:
        d = input()
        contador = contador+1
    print(f"El número de intentos ha sido: {contador}")

Ejercicio()