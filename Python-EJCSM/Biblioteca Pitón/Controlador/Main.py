from Modelo.Biblioteca import Biblioteca
from Modelo.Usuario import Usuario
from Vista import Vista as vista
import os

directorioActual = os.path.dirname(__file__)
raizProyecto = os.path.join(directorioActual, "..")
rutaLibros = os.path.join(raizProyecto, "Vista", "bbddLibros", "bbddLibros.txt")
rutaUsuarios = os.path.join(raizProyecto, "Vista", "bbddUsuarios.txt")

biblioteca = Biblioteca(rutaLibros, rutaUsuarios)
vista.biblioteca = biblioteca

def menuPrincipal():
    while (True):
        vista.menuPrincipal()
        opcion = vista.pedirOpcion()
        match (opcion):
            case 1:
                usuario = vista.iniciarSesionUsuario(biblioteca)
                if (usuario is not None):
                    subMenu(usuario, False)
                else:
                    continue
            case 2:
                nuevoUsuario = vista.registrarUsuario(biblioteca)
                subMenu(nuevoUsuario, True)
            case 3:
                vista.despedida()
                break
            case _:
                vista.opcionIncorrecta()

def subMenu(usuario : Usuario, nuevoUsuario : bool):
    while (True):
        vista.subMenu(usuario, nuevoUsuario)
        opcion = vista.pedirOpcion()
        match (opcion):
            case 1:
                vista.verListadoLibros(biblioteca)
            case 2:
                vista.verMisLibros(usuario)
            case 3:
                vista.leerLibro(biblioteca)
            case 4:
                vista.corregirLibro(biblioteca, usuario)
            case 5:
                vista.borrarLibro(biblioteca, usuario)
            case 6:
                vista.escribirLibro(biblioteca, usuario)
            case 7:
                vista.sesionCerrada()
                break
            case _:
                vista.opcionIncorrecta()

if __name__ == "__main__":
    menuPrincipal()