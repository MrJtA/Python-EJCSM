from Clases import Alumno, Profesor, Asignatura
from collections.abc import Iterable

listaAlumnos = []
listaProfesores = []
listaAsignaturas = []
asignaturas = {}

alumno = Alumno("Sara", "Larroda", 19)
listaAlumnos.append(alumno)
profesor = Profesor("Daniel", "Bartolomé", "danibat", "goku123")
listaProfesores.append(profesor)
asignatura = Asignatura("ADAT", "1", profesor)
listaAsignaturas.append(asignatura)

def pedirNombre():
    nombre = input("Introduce el nombre: ")
    return nombre

def matricularAlumno():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    edad = int(input("Introduce la edad: "))
    alumno = Alumno(nombre, apellido, edad)
    listaAlumnos.append(alumno)
    print("Se ha matriculado al alumno: ", alumno)

def buscarAlumno(nombre : str):
    for alumno in listaAlumnos:
        if nombre == alumno.nombre:
            print(alumno)
            return alumno
    else:
        print("No se ha encontrado a ningún alumno con ese nombre.")
        return None

def mostrarLista(lista):
    if not lista:
        print("La lista está vacía.")
        return
    else:
        for i in lista:
            print(i)

def matricularProfesor():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    usuario = input("Introduce el usuario: ")
    contraseña = input("Introduce la contraseña.")
    profesor = Profesor(nombre, apellido, usuario, contraseña)
    listaProfesores.append(profesor)
    print("Se ha matriculado al profesor: ", profesor)

def buscarProfesor(nombre : str):
    for profesor in listaProfesores:
        if nombre == profesor.nombre:
            print(profesor)
            return profesor
    else:
        print("No se ha encontrado a ningún profesor con ese nombre.")
        return None

def crearAsignatura():
    nombre = input("Introduce el nombre: ")
    codigo = input("Introduce el código: ")
    if not listaProfesores:
        print("No hay ningún profesor matriculado.")
        return
    profesor = None
    while True:
        print("Se le asignará un profesor.")
        profesor = buscarProfesor(pedirNombre())
        if profesor is None:
            continue
        else: break
    asignatura = Asignatura(nombre, codigo, profesor)
    profesor.listaAsignaturas.append(asignatura)
    print("Se ha creado la asignatura: ", asignatura)
    asignaturas[asignatura.codigo] = asignatura.listaAlumnos

def buscarAsignatura(codigo : str):
    for k, v in asignaturas.items():
        if k == codigo:
            print(k, v)
            return codigo
    else:
        print("No se ha encontrado a ningún asignatura con ese código.")
        return None

def matricularAlumnoAsignatura():
    print("Se indicará el nombre del alumno.")
    alumno = buscarAlumno(pedirNombre())
    if alumno is None:
        return
    print("Se indicará el código de la asignatura.")
    asignatura = buscarAsignatura(pedirNombre())
    for k, v in asignaturas.items():
        if k == asignatura:
            v.append(alumno)

def pedirNumero():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            return opcion
        except:
            print("Tienes que introducir un número.")

def menu():
    while True:
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
        match opcion:
            case 0:
                break
            case 1:
                matricularAlumno()
                continue
            case 2:
                buscarAlumno(pedirNombre())
                continue
            case 3:
                mostrarLista(listaAlumnos)
                continue
            case 4:
                matricularProfesor()
                continue
            case 5:
                buscarProfesor(pedirNombre())
                continue
            case 6:
                mostrarLista(listaProfesores)
                continue
            case 7:
                crearAsignatura()
                continue
            case 8:
                buscarAsignatura(pedirNombre())
                continue
            case 9:
                mostrarLista(listaAsignaturas)
                continue
            case 10:
                matricularAlumnoAsignatura()
            case _:
                print("Introduce una opción válida.")
                continue

print("Bienvenido al instituto IES Lope de Vega.")
menu()