class Usuario:

    def __init__(self, nombre : str, ID : int, contraseña : str):
        self.nombre = nombre
        self.ID = ID
        self.__contraseña = contraseña
        self.bbddLibros = {}

    def __str__(self) -> str:
        return (f"{self.nombre}: {self.ID}")

    @property
    def contraseña(self):
        return self.__contraseña