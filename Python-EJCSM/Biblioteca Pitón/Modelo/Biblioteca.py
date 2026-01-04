from Modelo.Libro import Libro
from Modelo.Autor import Autor
from Modelo.Usuario import Usuario
import random, os

class Biblioteca:

    def __init__(self, rutaLibros : str, rutaUsuarios : str):
        self.rutaLibros = rutaLibros.strip()
        self.rutaUsuarios = rutaUsuarios.strip()
        self.bbddAutores = {}
        self.bbddUsuarios = self.cargarUsuarios()
        self.bbddLibros = self.cargarLibros()
        self.directorioActual = os.path.dirname(__file__)
        self.rutaCarpeta = os.path.abspath(os.path.join(self.directorioActual, "..", "Vista", "bbddLibros"))

    def cargarLibros(self) -> dict:
        try:
            auxLibros = {}
            with open(self.rutaLibros, "r", encoding="utf-8") as bbddLibros:
                for linea in bbddLibros:
                    linea = linea.strip()
                    if not linea:
                        continue
                    dato = linea.split(";")
                    if len(dato) < 3:
                        continue
                    titulo = dato[0]
                    nombreAutor = dato[1]
                    ruta = dato[2]
                    autor = Autor(nombreAutor)
                    libro = Libro(titulo, autor, ruta)
                    for usuario in self.bbddUsuarios.values():
                        if nombreAutor == usuario.nombre:
                            usuario.bbddLibros[libro.titulo] = libro
                    auxLibros[titulo] = libro
                    self.bbddAutores[nombreAutor] = autor
            return auxLibros
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los libros no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la base de datos de los libros.")
        except Exception as e:
            print(f"Error: {type(e)}")

    def escribirLibros(self):
        try:
            with open(self.rutaLibros, "w", encoding="utf-8") as bbddLibros:
                for libro in self.bbddLibros.values():
                    bbddLibros.write(f"{libro.titulo};{libro.autor};{libro.ruta};")
                    bbddLibros.write("\n")
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los libros no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la base de datos de los libros.")
        except Exception as e:
            print(f"Error: {type(e)}")

    def cargarUsuarios(self) -> dict:
        try:
            auxUsuarios = {}
            with open(self.rutaUsuarios, "r", encoding="utf-8") as bbddUsuarios:
                for linea in bbddUsuarios:
                    linea = linea.strip()
                    if not linea:
                        continue
                    dato = linea.split(";")
                    if len(dato) < 3:
                        continue
                    nombre = dato[0]
                    ID = int(dato[1])
                    contraseña = dato[2]
                    usuario = Usuario(nombre, ID, contraseña)
                    autor = Autor(nombre)
                    auxUsuarios[usuario.ID] = usuario
                    self.bbddAutores[nombre] = autor
            return auxUsuarios
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los usuarios no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la base de datos de los usuarios.")
        except Exception as e:
            print(f"Error: {type(e)}")

    def escribirUsuarios(self):
        try:
            with open(self.rutaUsuarios, "w", encoding="utf-8") as bbddUsuarios:
                for usuario in self.bbddUsuarios.values():
                    bbddUsuarios.write(f"{usuario.nombre};{usuario.ID};{usuario.contraseña};")
                    bbddUsuarios.write("\n")
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los usuarios no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la base de datos de los usuarios.")
        except Exception as e:
            print(f"Error: {type(e)}")

    def iniciarSesionUsuario(self) -> Usuario:
        print("Introduce 'exit' para salir.")
        print("En caso de haber olvidado tu ID, pulsa ENTER para iniciar el proceso de recuperación.")
        while (True):
            ID = input("Introduce tu ID: ")
            if ID == "exit":
                return None
            elif ID == "":
                ID = self.recuperacionID()
                if ID is None:
                    continue
                break
            elif not ID.isdigit():
                print("Error: El ID debe ser un número entero.")
                continue
            elif int(ID) not in self.bbddUsuarios:
                print("El ID no está registrado en la base de datos. Asegúrese de usar un usuario existente, o registre un nuevo usuario.")
                continue
            else:
                break
        usuario = self.bbddUsuarios[int(ID)]
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

    def recuperacionID(self):
        print("Iniciando proceso de recuperación de ID.")
        print("Introduce 'exit' para salir.")
        while True:
            nombre = input("Introduce tu nombre: ").strip()
            if nombre == 'exit':
                return None
            for usuario in self.bbddUsuarios.values():
                if usuario.nombre == nombre:
                    idRecuperado = usuario.ID
                    print(f"Se ha encontrado el ID: {idRecuperado} a nombre de '{nombre}'.")
                    return idRecuperado

    def registrarUsuario(self) -> Usuario:
        while True:
            nombre = input("Introduce tu nombre: ").strip()
            contraseña = input("Introduce tu contraseña: ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue
            elif nombre in self.bbddAutores:
                print(f"El nombre '{nombre}' ya está cogido.")
                continue
            elif nombre == "exit" or contraseña == "exit":
                print("No se permite poner ese nombre o contraseña.")
                continue
            else:
                break
        ID = random.randint(1000, 9999)
        while ID in self.bbddUsuarios:
            ID = random.randint(1000, 9999)
        print("Se le ha asignado el siguiente ID numérico con el que debe acceder en futuros inicios de sesión: ")
        print(ID)
        nuevoUsuario = Usuario(nombre, ID, contraseña)
        self.bbddUsuarios[ID] = nuevoUsuario
        self.escribirUsuarios()
        return nuevoUsuario