class Autor:

    def __init__(self, nombre : str):
        self.nombre = nombre
        self.bbddLibros = {}

    def __str__(self) -> str:
        return self.nombre