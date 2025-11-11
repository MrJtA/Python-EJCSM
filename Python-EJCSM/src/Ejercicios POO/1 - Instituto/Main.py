from Clases import Alumno, Profesor, Asignatura

listaAlumnos = []
listaProfesores = []
listaAsignaturas = {}

def pedirNombre():
    nombre = input("Introduce el nombre: ")
    return nombre

def matricularAlumno():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    edad = input("Introduce la edad: ")
    alumno = Alumno(nombre, apellido, edad)
    listaAlumnos.append(alumno)

def buscarAlumno(nombre : str):
    for alumno in listaAlumnos:
        if nombre == alumno.nombre:
            print(alumno)
    else:
        print("No se ha encontrado a ningún alumno con ese nombre.")

def mostrarLista(lista):
    if isinstance(lista, dict):
        for k in listaAsignaturas.keys():
            print(k)
    elif isinstance(lista, lista.abc.Iterable):
        for i in lista:
            print(i)

def matricularProfesor():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    usuario = input("Introduce el usuario: ")
    contraseña = input("Introduce la contraseña.")
    profesor = Profesor(nombre, apellido, usuario, contraseña)
    listaProfesores.append(profesor)

def buscarProfesor(nombre : str):
    for profesor in listaProfesores:
        if nombre == profesor.nombre:
            print(profesor)
    else:
        print("No se ha encontrado a ningún profesor con ese nombre.")

def crearAsignatura():
    nombre = input("Introduce el nombre: ")
    codigo = input("Introduce el código: ")
    while True:
        profesor = input("Introduce el profesor: ")
        if profesor not in listaProfesores:
            print("El profesor no está matriculado.")
            continue
        else: break
    asignatura = Asignatura(nombre, codigo, profesor)
    listaAsignaturas[asignatura.codigo] = asignatura.listaAlumnos

def buscarAsignatura(codigo : str):
    for asignatura in listaAsignaturas.keys():
        if codigo == asignatura.codigo:
            print(asignatura)
    else:
        print("No se ha encontrado a ningún asignatura con ese código.")

def pedirNumero():
    while True:
        try:
            opcion = int(input("Introduce una opción."))
            return opcion
        except:
            print("Tienes que introducir un número.")

def menu():
    print("0. Salir.")
    print("1. Matricular un alumno.")
    print("2. Buscar un alumno.")
    print("3. Mostrar todos los alumnos.")
    print("4. Matricular un profesor.")
    print("5. Buscar un profesor.")
    print("6. Mostrar todos los profesores.")
    print("7. Crear asignatura")
    print("8. Buscar una asignatura por código.")
    print("9. Mostrar todas las asignaturas.")
    print("10. Matricular un alumno en una asignatura.")
    opcion = pedirNumero()
    while True:
        match opcion:
            case 0:
                break
            case 1:
                matricularAlumno()
            case 2:
                buscarAlumno(pedirNombre())
            case 3:
                mostrarLista(listaAlumnos)
            case 4:
                matricularProfesor()
            case 5:
                buscarProfesor(pedirNombre())
            case 6:
                mostrarLista(listaProfesores)
            case 7:
                crearAsignatura()
            case 8:
                buscarAsignatura(pedirNombre())
            case _:
                print("Introduce una opción válida.")
                continue

print("Bienvenido al instituto IES Lope de Vega.")
menu()