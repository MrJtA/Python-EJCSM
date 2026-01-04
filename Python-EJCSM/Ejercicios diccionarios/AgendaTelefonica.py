diccionario = {}

def verContactos():
    if not diccionario:
        print("No hay registrado ningún contacto.")
    else:
        print(f"A continuación se muestran los contactos registrados: {diccionario}")

def añadirContacto():
    n = input("Introduce el nombre: ")
    t = int(input("Introduce el número de teléfono: "))
    diccionario[n] = t

def buscarContacto():
    c = input("Introduce el nombre o el número de teléfono del contacto: ")
    ey = None
    if diccionario:
        for k, v in diccionario.items():
            if c == k or c == v:
                print(f"Nombre: {k}, Nº de teléfono: {v}")
                ey = k
                break
        else:
            print("No se ha encontrado ningún contacto así.")
    else:
        print("No hay ningún contacto registrado.")
    return ey

def borrarContacto():
    ey = buscarContacto()
    if ey != None:
        del diccionario[ey]
        print(f"El contacto con nombre '{ey}' se ha borrado correctamente.")

print("Bienvenido.")
n = 0
while n<5:
    print("1. Ver contactos.")
    print("2. Añadir contacto.")
    print("3. Buscar contacto.")
    print("4. Borrar contacto.")
    print("5. Salir.")
    n = int(input("Seleccione una opción: "))
    match n:
        case 1:
            verContactos()
        case 2:
            añadirContacto()
        case 3:
            buscarContacto()
        case 4:
            borrarContacto()
        case 5:
            print("Muchas gracias por su visita.")