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
        print("1. Leer todo el fichero.")
        print("2. Leer línea a línea por introducción de ENTER.")
        print("3. Añadir línea.")
        opcion = pedirNumero()
        match opcion:
            case 0:
                break
            case 1:
                leerFichero()
                continue
            case 2:
                leerLinea()
                continue
            case 3:
                añadirLinea()
                continue
            case _:
                print("Introduce una opción válida.")
                continue

menu()