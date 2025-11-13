class Alumno:

    def __init__(self, nombre, apellido, edad : int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.listaAsignaturas = []

    def __str__(self) -> str:
        return str(f"Alumno: {self.nombre}, {self.apellido}. Edad: {self.edad}")

class Profesor:

    def __init__(self, nombre, apellido, user, password):
        self.nombre = nombre
        self.apellido = apellido
        self.__user = user
        self.__pasword = password
        self.listaAsignaturas = []

    def __str__(self) -> str:
        return str(f"Profesor: {self.nombre}, {self.apellido}.")

class Asignatura:

    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.listaAlumnos = []

    def __str__(self) -> str:
        return str(f"Asignatura: {self.nombre}, Código: {self.apellido}, Profesor: {self.profesor}.")

    @property
    def setProfesor(self, nombreProfesor):
        self.profesor = nombreProfesor