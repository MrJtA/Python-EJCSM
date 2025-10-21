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