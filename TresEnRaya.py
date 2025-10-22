import random

posiciones = {}
historialPosiciones1 = {}
historialPosiciones2 = {}

for i in (1, 2, 3):
    for j in ("A", "B", "C"):
        posiciones[str(i)+j] = (i, j)

def dibujarTablero():
    print("    A  -  B  -  C")
    for i in (1, 2, 3):
        print(i, end=" ")
        for j in ("A", "B", "C"):
            if (i, j) in historialPosiciones1.values(): print("  X  ", end="")
            elif (i, j) in historialPosiciones2.values(): print("  O  ", end="")
            else: print("  _  ", end="")
            if not j == "C": print("|", end="")
        if not i == 3: print("\n   ---------------")
    print("\n")

def pedirModalidad():
    opcion = 0
    while opcion not in (1, 2):
        print("Bienvenido al juego 3 en raya.")
        print("1. Jugar contra otro jugador.")
        print("2. Jugar contra el ordenador.")
        opcion = int(input("Seleccione una opción: "))
        if opcion not in(1, 2):
            print("Introduce una opción válida.")
    return opcion

def pedirModalidad2():
    opcion = 0
    while opcion not in (1, 2):
        print("Elige la modalidad de las fichas: ")
        print("1. 4 fichas inamovibles. El juego termina cuando se acaban las fichas o cuando hay un ganador.")
        print("2. 3 fichas movibles. El juego sólo termina si hay un ganador.")
        opcion = int(input("Seleccione una opción: "))
        if opcion not in(1, 2):
            print("Introduce una opción válida.")
    return opcion

def pedirPosicion(jugador):
    while True:
        posicion = input(f"Jugador {jugador}, introduce la posición: ")
        if posicion in posiciones:
            break
        print("Introduce una posición válida o disponible. La posición debe escribirse con el número (fila) seguido de la letra en mayúscula (columna).")
    return posicion

def registrarMovimiento(opcion2, posicion, historialPosiciones, fichas):
    if opcion2 == 2 and fichas <= 0:
        primera_posicion = list(historialPosiciones.keys())[0]
        coordenada = historialPosiciones.pop(primera_posicion)
        posiciones[primera_posicion] = coordenada
    coordenada_nueva = posiciones[posicion]
    del posiciones[posicion]
    historialPosiciones[posicion] = coordenada_nueva
    dibujarTablero()

def comprobarGanador(jugador, historialPosiciones):
    for columna in ("A", "B", "C"):
        if (1, columna) in historialPosiciones.values() and (2, columna) in historialPosiciones.values() and (3, columna) in historialPosiciones.values():
            return True
    for fila in (1, 2, 3):
        if (fila, "A") in historialPosiciones.values() and (fila, "B") in historialPosiciones.values() and (fila, "C") in historialPosiciones.values():
            return True
    if (1, "A") in historialPosiciones.values() and (2, "B") in historialPosiciones.values() and (3, "C") in historialPosiciones.values():
        return True
    if (1, "C") in historialPosiciones.values() and (2, "B") in historialPosiciones.values() and (3, "A") in historialPosiciones.values():
        return True
    return False

# Esta función hace casi todo en uno: Pide la entrada de la posición, comprueba si es válida, registra el movimiento, actualiza el cuadro y comprueba si hay ganador.
def operar(opcion, opcion2, jugador, fichas, historialPosiciones):
    if opcion == 1:
        posicion = pedirPosicion(jugador)
    elif opcion == 2:
        posicion = random.choice(list(posiciones))
        registrarMovimiento(opcion2, posicion, historialPosiciones, fichas)
        registrarMovimiento(opcion2, posicion, historialPosiciones, fichas)
    if comprobarGanador(jugador, historialPosiciones):
        print(f"El jugador {jugador} ha ganado.")

def turnos():
    opcion = pedirModalidad()
    opcion2 = pedirModalidad2()
    if opcion2 == 1: fichas1 = fichas2 = 4
    elif opcion2 == 2: fichas1 = fichas2 = 3
    while True:
        operar(1, opcion2, 1, fichas1, historialPosiciones1)
        if comprobarGanador(1, historialPosiciones1):
            break
        operar(opcion, opcion2, 2, fichas2, historialPosiciones2)
        if comprobarGanador(2, historialPosiciones2):
            break
        if opcion2 == 1:
            fichas1 -= 1
            fichas2 -= 1
        if opcion2 == 1 and fichas1 == fichas2 == 0:
            print("Se han acabado las fichas y nadie ha ganado. Se da como un empate.")
            break
    print("Fin del juego, gracias por jugar.")

dibujarTablero()
turnos()