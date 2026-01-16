def leerFichero():
    try:
        with open("ejemplo.txt", "r") as fichero:
            for linea in fichero.readlines():
                print(linea, end="")
        print()
    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print("Error misterioso: ", type(e))

def crearFichero():
    nombreFichero = input("Introduce el nombre del fichero: ")
    nombreFichero += ".txt"
    try:
        with open(nombreFichero, "w") as fichero:
            fichero.write(f"Fichero creado con nombre '{nombreFichero}'.")
            fichero.write("\n")
        print("El fichero se ha creado correctamente.")
    except IOError:
        print("Error en los flujos de entrada y salida.")
    except PermissionError:
        print("No tienes permisos para crear un fichero.")
    except Exception as e:
        print("Error: ", type(e))

def leerLinea():
    try:
        with open("ejemplo.txt", "r") as fichero:
            for linea in fichero.readlines():
                print(linea, end="")
                input()
        print()
    except FileNotFoundError:
        print("El fichero no existe.")
    except EOFError:
        print("Llegaste al final.")
    except Exception as e:
        print("Error misterioso: ", type(e))

def añadirLinea():
    try:
        with open("ejemplo.txt", "a") as fichero:
            nuevaLinea = input("Introduce la línea: ")
            fichero.write("\n")
            fichero.write(nuevaLinea)
        print()
    except FileNotFoundError:
        print("El fichero no existe.")
    except IOError:
        print("Error al escribir el archivo.")
    except Exception as e:
        print("Error misterioso: ", type(e))

def pedirNumero():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            return opcion
        except:
            print("Tienes que introducir un número.")

def menu():
    print("Bienvenido.")
    while True:
        print("0. Salir.")
        print("1. Crear un fichero.")
        print("2. Leer todo el fichero.")
        print("3. Leer línea a línea por introducción de ENTER.")
        print("4. Añadir línea.")
        opcion = pedirNumero()
        match opcion:
            case 0:
                break
            case 1:
                crearFichero()
            case 2:
                leerFichero()
                continue
            case 3:
                leerLinea()
                continue
            case 4:
                añadirLinea()
                continue
            case _:
                print("Introduce una opción válida.")
                continue

menu()