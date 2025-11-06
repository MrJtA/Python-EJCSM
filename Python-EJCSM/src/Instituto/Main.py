from Clases import Aula, Alumno

aula = Aula("IES Lope de Vega")

def matricularAlumno():
    nombre = input("Introduce el nombre:")
    dni = input("Introduce el dni:")
    telefono = input("Introduce el telefono:")
    usuario = input("Introduce el usuario:")
    contraseña = input("Introduce el contraseña:")
    alumno = Alumno(nombre, dni, telefono, usuario, contraseña)
    Alumno.matricularAlumno(alumno)

def pedirNumero():
    while True:
        try:
            opcion = int(input("Introduce una opción."))
            return opcion
        except:
            print("Tienes que introducir un número.")

def menu():
    print("Bienvenido al instituto ", aula.nombre)
    print("0. Salir.")
    print("1. Matricular un alumno.")
    print("2. Buscar un alumno.")
    print("3. Mostrar todos los alumnos matriculados.")
    print("4. Modificar los datos de un alumno.")
    opcion = pedirNumero()
    while True:
        match (opcion):
            case 0: break
            case 1: matricularAlumno()
            case 3: aula.mostrarAlumnos()
            case _: print("No has selecionado ninguna opción valida")

menu()