class Alumno:

    def __init__(self, nombre, apellido, edad, listaAsignaturas):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        listaAsignaturas = []

    def __str__(self) -> str:
        return str(f"Alumno: {self.nombre}, {self.apellido}. Edad: {self.edad}")

class Profesor:

    def __init__(self, nombre, apellido, user, password, listaAsignaturas):
        self.nombre = nombre
        self.apellido = apellido
        self.__user = user
        self.__pasword = password
        listaAsignaturas = []

    def __str__(self) -> str:
        return str(f"Profesor: {self.nombre}, {self.apellido}.")

class Asignatura:

    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.listaAlumnos = []

    @property
    def setProfesor(self, nombreProfesor):
        self.profesor = nombreProfesor