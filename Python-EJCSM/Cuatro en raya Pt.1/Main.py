try:
    from Clases import Player, Game
except ImportError:
    print("Error al importar: Las clases no existen.")

def nombrarJugador(ficha : str):
    nombre = input(f"Introduce el nombre del jugador con ficha {ficha}: ")
    jugador = Player(nombre, ficha)
    return jugador

def pedirNumero(mensaje : str = "") -> int:
    while (True):
        try:
            numero = int(input(mensaje))
        except ValueError:
            print("Error: Introduce un valor adecuado.")
        else:
            return numero

def definirTablero(jugadorX, jugadorO):
    print("1. Jugar con el tablero por defecto (6 filas y 7 columnas).")
    print("2. Jugar con un tablero personalizado.")
    while (True):
        opcion = pedirNumero("Introduce una opción: ")
        match (opcion):
            case 1:
                juego = Game(jugadorX, jugadorO)
                break
            case 2:
                filas = pedirNumero("Introduce las filas: ")
                columnas = pedirNumero("Introduce las columnas: ")
                juego = Game(jugadorX, jugadorO, filas, columnas)
                break
            case _:
                print("Error: Introduce una opción válida.")
                continue
    return juego

def pedirPosicion(juego):
    while (True):
        try:
            columna = pedirNumero("Introduce la columna en la que quieres colocar la ficha: ")
            juego.colocarFicha(columna)
            break
        except IndexError:
            print("Error: Introduce un número de columna disponible.")
    juego.imprimirTablero()


def jugar():
    print("Bienvenido al juego 4 en raya.")
    jugadorX = nombrarJugador("X")
    jugadorO = nombrarJugador("O")
    juego = definirTablero(jugadorX, jugadorO)
    juego.imprimirTablero()
    while (True):
        print(f"Turno de {jugadorX}.")
        pedirPosicion(juego)
        if juego.victoria():
            print(f"Ha ganado {jugadorX}.")
            break
        print(f"Turno de {jugadorO}.")
        pedirPosicion(juego)
        if juego.victoria():
            print(f"Ha ganado {jugadorO}.")
            break

jugar()