from Modelo.Usuario import Usuario
from Modelo.Biblioteca import Biblioteca
from Modelo.Libro import Libro
import random, os

directorioActual = os.path.dirname(__file__)
raizProyecto = os.path.join(directorioActual, "..")
rutaLibros = os.path.join(raizProyecto, "Vista", "bbddLibros", "bbddLibros.txt")
rutaUsuarios = os.path.join(raizProyecto, "Vista", "bbddUsuarios.txt")

biblioteca = Biblioteca(rutaLibros, rutaUsuarios)

def pedirOpcion() -> int:
    while True:
        try:
            numero = int(input("Seleccione una opción: "))
            return numero
        except ValueError:
            print("Error: Introduce un número entero por favor.")

def menuPrincipal():
    print("-----------------------------------------------------------------------")
    print("\t\t\t\t\t- BIENVENIDO A PITON LIBRARY -")
    print("\t\t\t\t\t\t1. Iniciar sesión")
    print("\t\t\t\t\t\t2. Registrarse")
    print("\t\t\t\t\t\t3. Salir")
    print("-----------------------------------------------------------------------")

def subMenu(usuario : Usuario, nuevoUsuario : bool):
    print("-----------------------------------------------------------------------")
    if nuevoUsuario:
        print(f"\t\t\t\t\t- Bienvenido, {usuario.nombre} -")
    else:
        print(f"\t\t\t\t\t- Hola de nuevo, {usuario.nombre} -")
    print("\t\t\t\t\t\t1. Ver libros")
    print("\t\t\t\t\t\t2. Ver mis libros")
    print("\t\t\t\t\t\t3. Leer libro")
    print("\t\t\t\t\t\t4. Corregir libro")
    print("\t\t\t\t\t\t5. Borrar libro")
    print("\t\t\t\t\t\t6. Escribir libro")
    print("\t\t\t\t\t\t7. Cerrar sesión")
    print("-----------------------------------------------------------------------")
    
def despedida():
    print("Muchas gracias por su visita.")

def opcionIncorrecta():
    print("Por favor, seleccione una opción válida.")

def sesionCerrada():
    print("Sesión cerrada.")
    
def verListadoLibros(biblioteca):
    print("Libros disponibles, ordenados por autor alfabéticamente: ")
    for libro in sorted(biblioteca.bbddLibros.values()):
        print(f"\t- {libro}")

def verMisLibros(usuario : Usuario) -> dict:
    if not usuario.bbddLibros:
        print("Ahora mismo no tienes libros disponibles.")
        return None
    numeroLibrosDisponibles = 0
    librosDisponibles = {}
    for libro in sorted(usuario.bbddLibros.values()):
        numeroLibrosDisponibles += 1
        print(f"\t{numeroLibrosDisponibles}. {libro}")
        librosDisponibles[numeroLibrosDisponibles] = libro
    return librosDisponibles

def leerLibro(biblioteca):
    print("Introduce 'exit' para salir.")
    while True:
        encontrado = False
        numeroLibrosDisponibles = 0
        librosDisponibles = {}
        palabraBuscar = input("Buscar libros: ").lower()
        if palabraBuscar == "exit":
            return
        if palabraBuscar == "":
            continue
        for libro in sorted(biblioteca.bbddLibros.values()):
            if palabraBuscar in libro.titulo.lower() or palabraBuscar in str(libro.autor).lower():
                encontrado = True
                numeroLibrosDisponibles += 1
                print(f"\t{numeroLibrosDisponibles}. {libro}")
                librosDisponibles[numeroLibrosDisponibles] = libro
        if not encontrado:
            print("No se ha encontrado ningún libro relacionado.")
            continue
        opcion = input("Introduce la opción correspondiente para leer el libro, o pulsa ENTER para volver a buscar: ")
        if not opcion.isdigit() or int(opcion) not in librosDisponibles:
            print("Introduce una opción válida por favor.")
            continue
        libro = librosDisponibles[int(opcion)]
        ruta = os.path.join(biblioteca.rutaCarpeta, libro.ruta)
        if libro.contenido == "":
            print("Lo sentimos, el libro actualmente no tiene contenido.")
            continue
        print(f"El libro '{libro.titulo} tiene {libro.lineas} líneas.")
        if libro.lineas > 10:
            print("A continuación se mostrará el contenido del libro hasta 10 líneas.")
            print("Para leer el resto de líneas, pulsa ENTER por cada línea.")
        else:
            print("A continuación se muestra el contenido.")
        print("Introduce 'exit' para volver al buscador.")
        print()
        try:
            with open(ruta, "r", encoding="utf-8") as ficheroContenido:
                contador = 0
                for linea in ficheroContenido:
                    print(linea.strip())
                    contador += 1
                    if contador>10:
                        accion = input().lower()
                        if accion == "exit":
                            break
        except FileNotFoundError:
            print(f"Error: La ruta del contenido del libro '{libro.titulo}' no se ha podido encontrar.")
        except IOError:
            print(f"Error: Fallo en la conexión con la ruta del contenido del libro '{libro.titulo}'.")
        except Exception as e:
            print(f"Error: {type(e)}")
        print()

def corregirLibro(biblioteca, usuario : Usuario):
    librosDisponibles = verMisLibros(usuario)
    if librosDisponibles is None:
        return
    while True:
        print("Introduce 'exit' para salir.")
        opcion = input("Introduce la opción correspondiente para corregir el libro: ")
        if opcion == "exit":
            return
        if opcion == "":
            continue
        elif not opcion.isdigit() or int(opcion) not in librosDisponibles:
            print("Introduce una opción válida por favor.")
            continue
        libro = librosDisponibles[int(opcion)]
        ruta = os.path.join(biblioteca.rutaCarpeta, libro.ruta)
        print(f"Se corregirá el libro '{libro.titulo}'.")
        print("A continuación se mostrará el contenido del libro línea por línea.")
        print("Para corregir una línea mostrada, escribe la misma línea corregida.")
        print("Para acabar y/o saltar una línea, pulsa ENTER.")
        print("Introduce 'exit' para volver al buscador.")
        try:
            lineasCorregidas = []
            with open(ruta, "r", encoding="utf-8") as ficheroContenido:
                for linea in ficheroContenido:
                    print(linea.strip())
                    accion = input().lower()
                    if accion == "exit":
                        lineasCorregidas.append(linea)
                        for resto in ficheroContenido:
                            lineasCorregidas.append(resto)
                        break
                    elif accion == "":
                        lineasCorregidas.append(linea)
                    else:
                        lineasCorregidas.append(accion + "\n")
            with open(ruta, "w", encoding="utf-8") as ficheroContenido:
                ficheroContenido.writelines(lineasCorregidas)
                print("Cambios guardados con éxito.")
            libro.definirContenido()
        except FileNotFoundError:
            print(f"Error: La ruta del contenido del libro '{libro.titulo}' no se ha podido encontrar.")
        except IOError:
            print(f"Error: Fallo en la conexión con la ruta del contenido del libro '{libro.titulo}'.")
        except PermissionError:
            print(f"Error: No hay permisos suficientes para gestionar la ruta '{libro.ruta}'.")
        except Exception as e:
            print(f"Error: {type(e)}")

def escribirLibro(biblioteca, usuario):
    while True:
        print("Introduce 'exit' para salir.")
        titulo = input("Introduce el título del libro: ")
        if titulo == "exit":
            return
        if titulo == "":
            continue
        nombreFichero = titulo.replace(" ", "_") + ".txt"
        ruta = os.path.join(biblioteca.rutaCarpeta, nombreFichero)
        print("Puedes empezar a escribir:")
        print()
        try:
            with open(ruta, "w", encoding="utf-8") as ficheroContenido:
                while (True):
                    linea = input()
                    if linea == "exit":
                        break
                    ficheroContenido.write(linea)
                    ficheroContenido.write("\n")
        except FileNotFoundError:
            print(f"Error: La ruta del contenido del libro '{titulo}' no se ha podido encontrar.")
        except IOError:
            print(f"Error: Fallo en la conexión con la ruta del contenido del libro '{titulo}'.")
        except PermissionError:
            print(f"Error: No hay permisos suficientes para gestionar la ruta '{nombreFichero}'.")
        except Exception as e:
            print(f"Error: {type(e)}")
        libro = Libro(titulo, usuario.nombre, nombreFichero)
        biblioteca.bbddLibros[libro.titulo] = libro
        usuario.bbddLibros[libro.titulo] = libro
        biblioteca.escribirLibros()
        break

def borrarLibro(biblioteca, usuario):
    librosDisponibles = verMisLibros(usuario)
    if librosDisponibles is None:
        return
    while True:
        print("Introduce 'exit' para salir.")
        opcion = input("Introduce la opción correspondiente para borrar el libro: ")
        if opcion == "exit":
            return
        elif opcion == "":
            continue
        elif not opcion.isdigit() or int(opcion) not in librosDisponibles:
            print("Introduce una opción válida por favor.")
            continue
        libro = librosDisponibles[int(opcion)]
        ruta = os.path.join(biblioteca.rutaCarpeta, libro.ruta)
        print(f"¿Está seguro de borrar permanentemente el libro '{libro.titulo}'?")
        confirmacion = input("Introduce 'exit' para salir o pulsa ENTER para confirmar: ")
        if confirmacion == "exit":
            print("Borrado cancelado.")
            libro.definirContenido()
            break
        try:
            if libro.titulo in biblioteca.bbddLibros:
                del biblioteca.bbddLibros[libro.titulo]
            if libro.titulo in usuario.bbddLibros:
                del usuario.bbddLibros[libro.titulo]
            if usuario.nombre in biblioteca.bbddAutores:
                autor = biblioteca.bbddAutores[usuario.nombre]
                if libro.titulo in autor.bbddLibros:
                    del autor.bbddLibros[libro.titulo]
            if os.path.exists(ruta):
                os.remove(ruta)
            biblioteca.escribirLibros()
            biblioteca.escribirUsuarios()
            print(f"El libro '{libro.titulo}' ha sido borrado con éxito.")
            break
        except FileNotFoundError:
            print(f"Error: La ruta del contenido del libro '{libro.titulo}' no se ha podido encontrar.")
        except IOError:
            print(f"Error: Fallo en la conexión con la ruta del contenido del libro '{libro.titulo}'.")
        except PermissionError:
            print(f"Error: No hay permisos suficientes para borrar la ruta '{libro.ruta}'.")
        except Exception as e:
            print(f"Error: {type(e)}")

def iniciarSesionUsuario(biblioteca) -> Usuario:
    print("Introduce 'exit' para salir.")
    print("En caso de haber olvidado tu ID, pulsa ENTER para iniciar el proceso de recuperación.")
    while True:
        ID = input("Introduce tu ID: ")
        if ID == "exit":
            return None
        elif ID == "":
            ID = recuperacionID(biblioteca)
            if ID is None:
                continue
            break
        elif not ID.isdigit():
            print("Error: El ID debe ser un número entero.")
            continue
        elif int(ID) not in biblioteca.bbddUsuarios:
            print("El ID no está registrado en la base de datos. Asegúrese de usar un usuario existente, o registre un nuevo usuario.")
            continue
        else:
            break
    usuario = biblioteca.bbddUsuarios[int(ID)]
    intentosFallidos = 0
    while (intentosFallidos != 3):
        contraseña = input("Introduce la contraseña: ")
        if contraseña == "exit":
            return None
        if contraseña != usuario.contraseña:
            print("Error: Contraseña incorrecta.")
            intentosFallidos += 1
            continue
        else:
            return usuario
    print("¿Olvidaste tu contraseña? Intente contactar con el desarrollador de la aplicación para recuperarla.")
    return None

def recuperacionID(biblioteca) -> int:
    print("Iniciando proceso de recuperación de ID.")
    print("Introduce 'exit' para salir.")
    while True:
        nombre = input("Introduce tu nombre: ").strip()
        if nombre == 'exit':
            return None
        for usuario in biblioteca.bbddUsuarios.values():
            if usuario.nombre == nombre:
                idRecuperado = usuario.ID
                print(f"Se ha encontrado el ID: {idRecuperado} a nombre de '{nombre}'.")
                return idRecuperado

def registrarUsuario(biblioteca) -> Usuario:
    while True:
        nombre = input("Introduce tu nombre: ").strip()
        contraseña = input("Introduce tu contraseña: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue
        elif nombre in biblioteca.bbddAutores:
            print(f"El nombre '{nombre}' ya está cogido.")
            continue
        elif nombre == "exit" or contraseña == "exit":
            print("No se permite poner ese nombre o contraseña.")
            continue
        else:
            break
    ID = random.randint(1000, 9999)
    while ID in biblioteca.bbddUsuarios:
        ID = random.randint(1000, 9999)
    print("Se le ha asignado el siguiente ID numérico con el que debe acceder en futuros inicios de sesión: ")
    print(ID)
    nuevoUsuario = Usuario(nombre, ID, contraseña)
    biblioteca.bbddUsuarios[ID] = nuevoUsuario
    biblioteca.escribirUsuarios()
    return nuevoUsuario