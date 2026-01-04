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

def defPosicion(opcion, lista):
    if opcion == 1:
        while True:
            posicion = input("Introduce la posición: ")
            if posicion in lista:
                return posicion
            print("Introduce una posición válida o disponible. La posición debe escribirse con el número (fila) seguido de la letra en mayúscula (columna).")    
    elif opcion == 2:
        return random.choice(list(lista.keys())) 

def registrarMovimiento(posicion, historialPosiciones):
    posicionNueva = posiciones[posicion]
    del posiciones[posicion]
    historialPosiciones[posicion] = posicionNueva
    dibujarTablero()

def registrarMovimiento2(posicionAntigua, posicionNueva, historialPosiciones):
    del historialPosiciones[posicionAntigua]
    historialPosiciones[posicionNueva] = posiciones[posicionNueva]
    del posiciones[posicionNueva]
    posiciones[posicionAntigua] = (int(posicionAntigua[0]), posicionAntigua[1])
    dibujarTablero()

def comprobarGanador(historialPosiciones):
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

def realizar(jugador, opcion, opcion2, historialPosiciones, fichas):
    if jugador == 1:
        print("Turno del jugador 1 (X).")
        posicionNueva = defPosicion(1, posiciones)
    if jugador == 2:
        print("Turno del jugador 2 (O).")
        posicionNueva = defPosicion(opcion, posiciones)
    if opcion2 == 2 and fichas == 0:
        if jugador == 1:
            print("¿Qué posición quieres quitar?")
            posicionAntigua = defPosicion(1, historialPosiciones)
        if jugador == 2:
            if opcion == 1:
                print("¿Qué posición quieres quitar?")
            posicionAntigua = defPosicion(opcion, historialPosiciones)
        registrarMovimiento2(posicionAntigua, posicionNueva, historialPosiciones)
    else:
        registrarMovimiento(posicionNueva, historialPosiciones)
        fichas -= 1
    return fichas

def turnos():
    opcion = pedirModalidad()
    opcion2 = pedirModalidad2()
    if opcion2 == 1: fichas1 = fichas2 = 4
    elif opcion2 == 2: fichas1 = fichas2 = 3
    while True:
        fichas1 = realizar(1, opcion, opcion2, historialPosiciones1, fichas1)
        if comprobarGanador(historialPosiciones1):
            print("El jugador 1 (X) ha ganado.")
            break
        fichas2 = realizar(2, opcion, opcion2, historialPosiciones2, fichas2)
        if comprobarGanador(historialPosiciones2):
            print("El jugador 2 (O) ha ganado.")
            break
        if opcion2 == 1 and fichas1 == 0 and fichas2 == 0:
            print("Se han acabado las fichas y nadie ha ganado. Se da como un empate.")
            break
    print("Fin del juego, gracias por jugar.")

dibujarTablero()
turnos()