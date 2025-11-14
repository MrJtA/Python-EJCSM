class Trabajador:

    def __init__(self, nombre : str, administrador : bool ):
        self.nombre = nombre
        self.administrador = administrador
        self.propina = 0.0

    def __str__(self) -> str:
        if self.administrador:
            return str(f"Nombre: {self.nombre}, Administrador. Propina recaudada: {self.propina}.")
        else:
            return str(f"Nombre: {self.nombre}, Empleado. Propina recaudada: {self.propina}.")

listaTrabajadores = []
recaudacion = 0.0
carta = {}

trabajador1 = Trabajador("Joaquin", True)
listaTrabajadores.append(trabajador1)
trabajador2 = Trabajador("Sara", False)
listaTrabajadores.append(trabajador2)
carta["Ceviche"] = [12.5, True]
carta["Agua"] = [0.5, False]

def mostrarTrabajadores():
    for trabajador in listaTrabajadores:
        print(trabajador)

def pedirNombre() -> str:
    nombre = input("Introduce el nombre: ")
    return nombre

def buscarTrabajador(nombre : str) -> Trabajador:
    if not listaTrabajadores:
        print("No hay ningún trabajador.")
        return
    for trabajador in listaTrabajadores:
        if trabajador.nombre == nombre:
            return trabajador

def contratarTrabajador(nombre):
    esAdmin = False
    conceder = input("En caso de que quieras concerder adminstración, introduce 'Si': ")
    if conceder == 'Si':
        esAdmin = True
    trabajador = Trabajador(nombre, esAdmin)
    listaTrabajadores.append(trabajador)

def pedirNumero():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            return opcion
        except:
            print("Tienes que introducir un número.")

def añadirPlato(nombre : str):
    precio = float(input("Introduce el precio: "))
    disponibilidad = False
    conceder = input("En caso de que quieras concerder disponibilidad, introduce 'Si': ")
    if conceder == 'Si':
        disponibilidad = True
    lista = [precio, disponibilidad]
    carta[nombre] = lista
    print(f"Plato '{nombre}' añadido a la carta.")

def cambiarPrecioPlato(nombre : str):
    if nombre not in carta:
        print("No se ha encontrado ningún plato con ese nombre.")
        return
    nuevoPrecio = float(input("Introduce el nuevo precio: "))
    carta[nombre][0] = nuevoPrecio
    print("Se ha cambiado el precio correctamente.")

def indicarDisponibilidad(nombre : str):
    if nombre not in carta:
        print("No se ha encontrado ningún plato con ese nombre.")
        return
    disponibilidad = False
    conceder = input("En caso de que quieras concerder disponibilidad, introduce 'Si':")
    if conceder == 'Si':
        disponibilidad = True
    carta[nombre][1] = disponibilidad
    print("Se ha cambiado la disponibilidad correctamente.")

def mostrarPlatos():
    if not carta:
        print("No hay ningún plato en la carta.")
    for nombrePlato, precioYdisponibilidad in carta.items():
        print(f"Nombre: {nombrePlato}. Precio: {precioYdisponibilidad[0]}. Disponible: {precioYdisponibilidad[1]}")

def mostrarRecaudación():
    print(f"Se ha recaudado un total de {recaudacion}€ por todos los platos vendidos.")

def venderPlato(nombre : str):
    global recaudacion
    if nombre not in carta:
        print("No se ha encontrado ningún plato con ese nombre.")
        return
    precio, disponible = carta[nombre]
    if not disponible:
        print(f"El plato '{nombre}' no está disponible actualmente.")
        return 0.0
    recaudacion += precio
    print("Se ha vendido el plato. Se le dará un 10% del precio del plato al camarero como propina.")
    return precio

def menu2(trabajador : Trabajador):
    if trabajador.administrador:
        while True:
            print("0. Salir")
            print("1. Añadir un plato.")
            print("2. Cambiar precio de un plato.")
            print("3. Indicar disponibilidad de un plato.")
            print("4. Mostrar todos los platos.")
            print("5. Mostrar recaudación.")
            opcion = pedirNumero()
            match opcion:
                case 0:
                    break
                case 1:
                    añadirPlato(pedirNombre())
                case 2:
                    cambiarPrecioPlato(pedirNombre())
                case 3:
                    indicarDisponibilidad(pedirNombre())
                case 4:
                    mostrarPlatos()
                case 5:
                    mostrarRecaudación()
                case _:
                    print("Introduce una opción válida.")
                    continue
    else:
        while True:
            print("0. Salir")
            print("1. Mostrar carta.")
            print("2. Vender plato.")
            opcion = pedirNumero()
            match opcion:
                case 0:
                    break
                case 1:
                    mostrarPlatos()
                case 2:
                    propina = venderPlato(pedirNombre())/10
                    trabajador.propina += propina
                case _:
                    print("Introduce una opción válida.")
                    continue

def menu():
    while True:
        print("Bienvenido al restaurante PK2 de orgullo.")
        print("0. Salir")
        print("1. Introducir tu nombre.")
        print("2. Mostrar trabajadores.")
        opcion = pedirNumero()
        match opcion:
            case 0:
                break
            case 1:
                nombre = pedirNombre()
                trabajador = buscarTrabajador(nombre)
                if trabajador:
                    menu2(trabajador)
            case 2:
                mostrarTrabajadores()
            case _:
                print("Introduce una opción válida.")
                continue

menu()