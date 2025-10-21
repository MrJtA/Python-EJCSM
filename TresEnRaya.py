import random

posiciones = {}
historialPosiciones1 = []
historialPosiciones2 = []

for i in (1, 2, 3):
    for j in ("A", "B", "C"):
        posiciones[str(i)+j] = (i, j)

def dibujarTablero():
    print("    A  -  B  -  C")
    for i in (1, 2, 3):
        print(i, end=" ")
        for j in ("A", "B", "C"):
            if str(i)+j in historialPosiciones1: print("  X  ", end="")
            elif str(i)+j in historialPosiciones2: print("  O  ", end="")
            else: print("  _  ", end="")
            if not j == "C": print("|", end="")
        if not i == 3: print("\n   ---------------")
    print("\n")

def existePosicion(posicion):
    if posicion in posiciones:
        return True
    else:
        print("Introduce una posición válida o disponible.")
        return False

def pedirModalidad():
    print("Bienvenido al juego 3 en raya.")
    print("1. Jugar contra otro jugador.")
    print("2. Jugar contra el ordenador.")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def registrarMovimientos(posicion, historialPosiciones, fichas):
    del posiciones[posicion]
    historialPosiciones.append(posicion)
    fichas -= 1
    dibujarTablero()

def turnos():
    fichas1 = fichas2 = 4
    opcion = pedirModalidad()
    while fichas2 > 0:
        posicion1 = input("Jugador 1, Introduce la posición: ")
        if existePosicion(posicion1):
            registrarMovimientos(posicion1, historialPosiciones1, fichas1)
        if opcion == 1:
            posicion2 = input("Jugador 2, Introduce la posición: ")
            if existePosicion(posicion2):
                registrarMovimientos(posicion2, historialPosiciones2, fichas2)
        if opcion == 2:
            posicion2 = random.choice(list(posiciones))
            registrarMovimientos(posicion2, historialPosiciones2, fichas2)
    print("Historial de posiciones del Jugador 1: ", historialPosiciones1)
    print("Historial de posiciones del Jugador 2: ", historialPosiciones2)

dibujarTablero()
turnos()