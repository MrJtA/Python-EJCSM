from Clases import Player, Game

rutaBBDD = "BB_DD.txt"
listaJugadores = {}

def cargarDatos():
    global rutaBBDD
    global listaJugadores
    try:
        with open(rutaBBDD, "r") as bbdd:
            for linea in bbdd.readlines():
                dato = linea.split(";")
                nombre = dato[0]
                simbolo = dato[1].strip()
                jugador = Player(nombre, simbolo)
                jugador.numeroVictorias = int(dato[2])
                jugador.rachaVictorias = int(dato[3])
                listaJugadores[jugador.token] = jugador
    except FileNotFoundError:
        print("El fichero no existe.")
    except IOError:
        print("Error al escribir el archivo.")
    except Exception as e:
        print("Error misterioso: ", type(e))

def nombrarJugador(numero : int):
    global listaJugadores
    print(f"Jugador {numero}.")
    nombre = input("Introduce el nombre: ")
    for jugador in listaJugadores.values():
        if jugador.name == nombre:
            print(f"Jugador registrado: {jugador}")
            jugador = listaJugadores[jugador.token]
            return jugador
    while True:
        ficha = input("Introduce la ficha: ")
        if ficha in listaJugadores.keys():
            print(f"La ficha '{ficha}' ya está en uso. Por favor, introduce una ficha diferente.")
            continue
        break
    jugador = Player(nombre, ficha)
    listaJugadores[ficha] = jugador
    return jugador

def pedirNumero(mensaje : str = "") -> int:
    while (True):
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Error: Introduce un valor adecuado.")
        else:
            return numero

def definirTablero(jugador1, jugador2):
    print("1. Jugar con el tablero por defecto (6 filas y 7 columnas).")
    print("2. Jugar con un tablero personalizado.")
    while (True):
        opcion = pedirNumero("Introduce una opción: ")
        match (opcion):
            case 1:
                juego = Game(jugador1, jugador2)
                break
            case 2:
                filas = pedirNumero("Introduce las filas: ")
                columnas = pedirNumero("Introduce las columnas: ")
                juego = Game(jugador1, jugador2, filas, columnas)
                break
            case _:
                print("Error: Introduce una opción válida.")
                continue
    return juego

def pedirPosicion(juego):
    while (True):
        try:
            columna = pedirNumero("Introduce la columna en la que quieres colocar la ficha: ")
            if juego.colocarFicha(columna):
                break
            else:
                print("Error: La columna está llena. Por favor, elige otra.")
                juego.imprimirTablero()
        except IndexError:
            print("Error: Introduce un número de columna disponible.")
    juego.imprimirTablero()

def jugar():
    jugador1 = nombrarJugador(1)
    while True:
        jugador2 = nombrarJugador(2)
        if jugador2.token == jugador1.token:
            print("Error: Un jugador no puede jugar contra sí mismo. Por favor, elige a otro jugador.")
        else:
            break
    juego = definirTablero(jugador1, jugador2)
    juego.imprimirTablero()
    while (True):
        print(f"Turno de {jugador1.nombre()}.")
        pedirPosicion(juego)
        if juego.victoria():
            print(f"Ha ganado {jugador1.nombre()}.")
            actualizarDatos(jugador1, jugador2)
            break
        print(f"Turno de {jugador2.nombre()}.")
        pedirPosicion(juego)
        if juego.victoria():
            print(f"Ha ganado {jugador2.nombre()}.")
            actualizarDatos(jugador2, jugador1)
            break

def verRanking():
    global listaJugadores
    indice = 1
    for jugador in sorted(listaJugadores.values()):
        print(f"\t{indice}. {jugador}")
        indice += 1

def actualizarDatos(ganador, perdedor):
    global rutaBBDD, listaJugadores
    ganador.numeroVictorias += 1
    ganador.rachaVictorias += 1
    perdedor.rachaVictorias = 0
    for jugador in listaJugadores.values():
        listaJugadores[jugador.token] = jugador
    try:
        with open(rutaBBDD, "w") as bbdd:
            for jugador in listaJugadores.values():
                linea = f"{jugador.name}; {jugador.token}; {jugador.numeroVictorias}; {jugador.rachaVictorias};"
                bbdd.write(linea)
                bbdd.write("\n")
        print("Datos guardados correctamente.")
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print("Error misterioso: ", type(e))

def menu():
    cargarDatos()
    print("Bienvenido al juego 4 en raya.")
    while True:
        print("0. Salir.")
        print("1. Jugar")
        print("2. Ver ranking de jugadores.")
        opcion = pedirNumero("Seleccione una opción: ")
        match opcion:
            case 0:
                break
            case 1:
                jugar()
                continue
            case 2:
                verRanking()
                continue
            case _:
                print("Seleccione una opción disponible.")

menu()