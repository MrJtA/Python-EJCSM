class Libro:

    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.prestado = False

    def __str__(self) -> str:
        if self.prestado:
            return str((self.titulo, self.autor, self.genero, "DISPONIBLE"))
        else:
            return str((self.titulo, self.autor, self.genero, "NO DISPONIBLE"))

    def __eq__(self, value) -> bool:
        if isinstance(value, Libro):
            return self.titulo == value.titulo and self.autor == value.autor
        return False

    def __lt__(self, value) -> bool:
        if self.titulo == value.titulo:
            return self.autor < value.autor
        else:
            return self.titulo < value.titulo

class Biblioteca:

    def __init__(self, nombre):
        self.titulo = nombre
        self.libros = []

    def __contains__(self, item) -> bool:
        return item in self.libros

    def agregarLibro(self, libro) -> None:
        if libro not in self.libros:
            self.libros.append(libro)
            self.libros.sort()
            print("El libro se ha agregado a la biblioteca.")
        else:
            print("El libro ya existe.")

    def buscarLibro(self, titulo) -> None:
        encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo:
                print(libro)
                encontrado = True
        if not encontrado:
            print("El libro no existe.")

    def buscarAutor(self, autor) -> None:
        encontrado = False
        for libro in self.libros:
            if libro.autor == autor:
                print(libro)
                encontrado = True
        if not encontrado:
            print("No existen libros de ese autor.")

    def buscarGenero(self, genero) -> None:
        encontrado = False
        for libro in self.libros:
            if libro.genero == genero:
                print(libro)
                encontrado = True
        if not encontrado:
            print("No existen libros de ese género.")

    def mostrarOrdenados(self):
        self.libros.sort()
        for libro in self.libros:
            print(libro)

    def prestarLibro(self, titulo) -> Libro:
        libro = self.buscarLibro(titulo)
        if libro not in self.libros:
            print("El libro no existe.")
            return None
        if libro.prestado:
            print("El libro ya está prestado.")
            return None
        else:
            libro.prestado = True
            return libro

    def devolverLibro(self, titulo) -> Libro:
        libro = self.buscarLibro(titulo)
        if libro not in self.libros:
            print("El libro no existe.")
            return None
        if not libro.prestado:
            print("El libro no está prestado.")
            return None
        else:
            libro.prestado = False
            return libro