class Alumno:

    profesorPython = "Dani"

    def __init__(self, nombre, dni, telefono, usuario, contraseña):
        self.nombre = nombre
        self.__dni = dni
        self.__telefono = telefono
        self.__usuario = usuario
        self.__contraseña = contraseña

    def __str__(self) -> str:
        return str(self.nombre)
    
    @property
    def dni(self):
        return self.__dni
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, numero : int):
        self.__telefono = numero
    
class Aula:

    def __init__(self, nombre):
        self.nombre = nombre
        self.delegado = ""
        self.alumnos = []

    def __str__(self) -> str:
        return str(self.nombre, self.delegado)
    
    def matricularAlumno(self, alumno) -> None:
        if alumno not in self.alumnos:
            self.alumnos.append(alumno)
        else:
            print("El alumno ya está matriculado.")

    def buscarAlumno(self, dni) -> Alumno:
        for alumno in self.alumnos:
            if alumno.dni == dni:
                return alumno
        return None

    def mostrarAlumnos(self):
        self.alumnos.sort
        for alumno in self.alumnos:
            print("\n", alumno)