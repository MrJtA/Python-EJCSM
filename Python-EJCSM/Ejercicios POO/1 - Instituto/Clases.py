class Alumno:

    def __init__(self, nombre, apellido, edad : int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.listaAsignaturas = {}

    def __str__(self) -> str:
        return str(f"Alumno: {self.nombre}, {self.apellido}. Edad: {self.edad}")

class Profesor:

    def __init__(self, nombre, apellido, user, password):
        self.nombre = nombre
        self.apellido = apellido
        self.__user = user
        self.__password = password
        self.listaAsignaturas = []

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    def __str__(self) -> str:
        return str(f"Profesor: {self.nombre}, {self.apellido}.")

class Asignatura:

    def __init__(self, codigo, nombre, profesor):
        self.codigo = codigo
        self.nombre = nombre
        self.profesor = profesor
        self.listaAlumnos = []

    def __str__(self) -> str:
        return str(f"Asignatura: {self.nombre}, Código: {self.codigo}, Profesor: {self.profesor.nombre}.")