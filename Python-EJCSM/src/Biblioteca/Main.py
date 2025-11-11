from Clases import Biblioteca, Libro

l1 = Libro("Niebla", "Miguel de Unamuno", "Ficción")
l2 = Libro("El barrio de la luz", "Inio Asano", "Manga")
l3 = Libro("Conversación en la catedral", "Mario Vargas Llosa", "Ficción")
l4 = Libro("La ciudad y los perros", "Mario Vargas Llosa", "Ficción")
l5 = Libro("Sapiens: De animales a dioses", "Yuval Noah Harari", "Historia")
l6 = Libro("Odisea", "Homero", "Épica")
l7 = Libro("Ilíada", "Homero", "Épica")
l8 = Libro("Ensayos Filosóficos", "Bertrand Rusell", "Filosofia")

biblioteca = Biblioteca("Biblioteca de Joaco.")
biblioteca.agregarLibro(l1)
biblioteca.agregarLibro(l2)
biblioteca.agregarLibro(l3)
biblioteca.agregarLibro(l4)
biblioteca.agregarLibro(l5)
biblioteca.agregarLibro(l6)
biblioteca.agregarLibro(l7)
biblioteca.agregarLibro(l8)

def pedirNumero(txt):
    while True:
        try:
            return int(input(txt))
        except:
            print("Tienes que introducir un número.")

def interfaz():
    while True:
        print("1. Buscar libro.")
        print("2. Buscar por autor.")
        print("3. Buscar por género.")
        print("4. Prestar libro.")
        print("5. Devolver libro.")
        print("6. Ver libros.")
        print("7. Salir.")
        opcion = pedirNumero("Opción : ")
        match opcion:
            case 1:
                titulo = input("Introduce el título: ")
                biblioteca.buscarLibro(titulo)
            case 2:
                autor = input("Introduce el autor: ")
                biblioteca.buscarAutor(autor)
            case 3:
                genero = input("Introduce el género: ")
                biblioteca.buscarGenero(genero)
            case 4:
                titulo = input("Introduce el título.")
                biblioteca.prestarLibro(titulo)
            case 5:
                titulo = input("Introduce el título.")
                biblioteca.devolverLibro(titulo)
            case 6:
                biblioteca.mostrarOrdenados()
            case 7:
                break
            case _:
                print("No has selecionado ninguna opción valida")

interfaz()