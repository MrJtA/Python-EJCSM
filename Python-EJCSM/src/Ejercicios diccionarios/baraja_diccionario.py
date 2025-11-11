import random

baraja = {}
valores = (1, 2, 3, 4, 5, 6 ,7, "Sota", "Caballo", "Rey")
palos = ("Oros", "Bastos", "Espadas", "Copas")

for v in valores:
    for p in palos:
        carta = (v, p)
        if isinstance(v, str):
        # if v == "Sota" or v == "Caballo" or v == "Rey":
        # if v in ("Sota", "Caballo", "Rey"):
        # if v in ["Sota", "Caballo", "Rey"]:
            baraja[carta] = 0.5
        else:
            baraja[carta] = v


mano_cartas = []
puntuacion = 0

seguir = True
while seguir:
    opcion  = int(input("Introduce un numero (1-2)")) 
    if opcion == 2:
        seguir = False
    else:
        lista_claves = list(baraja.keys())
        cRandom = random.choice(lista_claves)
        print(cRandom)
        mano_cartas.append(cRandom)
        punt_carta = baraja.get(cRandom)
        puntuacion += punt_carta

print(mano_cartas)
print(f"Tus puntos son : {puntuacion}")




