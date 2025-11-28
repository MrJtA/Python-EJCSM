class Player:

    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __str__(self):
        return(f"{self.name} ({self.token})")

class Game:

    def __init__(self, p1, p2, rows = 6, cols = 7):
        self.p1 = p1
        self.p2 = p2
        self.tablero = self.crearTablero(rows, cols)
        self.turno = True

    def crearTablero(self, rows, cols):
        t = []
        for _ in range(rows):
            f = []
            for _ in range(cols):
                f.append('-')
            t.append(f)
        return t

    def imprimirTablero(self):
        for fila in self.tablero:
            for c in fila:
                print(c, '', end='')
            print('')

    def colocarFicha(self, col):
        for i in range(len(self.tablero) - 1, -1, -1):
            if self.tablero[i][col] == '-':
                if self.turno:
                    self.tablero[i][col] = self.p1.token
                else:
                    self.tablero[i][col] = self.p2.token
                self.turno = not self.turno
                break

    def victoria(self) -> bool:
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        if not self.turno:
            token = self.p1.token
        else:
            token = self.p2.token
        # Verificar horizontal
        for fila in range(filas):
            for columna in range(columnas - 3):
                if (self.tablero[fila][columna] == token and
                    self.tablero[fila][columna + 1] == token and
                    self.tablero[fila][columna + 2] == token and
                    self.tablero[fila][columna + 3] == token):
                    return True
        # Verificar vertical
        for columna in range(columnas):
            for fila in range(filas - 3):
                if (self.tablero[fila][columna] == token and
                    self.tablero[fila + 1][columna] == token and
                    self.tablero[fila + 2][columna] == token and
                    self.tablero[fila + 3][columna] == token):
                    return True
        # Verificar diagonal (/)
        for fila in range(filas - 3):
            for columna in range(columnas - 3):
                if (self.tablero[fila][columna] == token and
                    self.tablero[fila + 1][columna + 1] == token and
                    self.tablero[fila + 2][columna + 2] == token and
                    self.tablero[fila + 3][columna + 3] == token):
                    return True
        # Verificar diagonal (\)
        for fila in range(3, filas):
            for columna in range(columnas - 3):
                if (self.tablero[fila][columna] == token and
                    self.tablero[fila - 1][columna + 1] == token and
                    self.tablero[fila - 2][columna + 2] == token and
                    self.tablero[fila - 3][columna + 3] == token):
                    return True
        return False