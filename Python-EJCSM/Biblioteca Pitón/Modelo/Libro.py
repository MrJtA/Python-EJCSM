from Modelo.Autor import Autor
import os

directorioActual = os.path.dirname(__file__)
rutaCarpetaContenidos = os.path.abspath(os.path.join(directorioActual, "..", "Vista", "bbddLibros"))

class Libro:

    def __init__(self, titulo : str, autor : Autor, ruta : str):
        self.titulo = titulo
        self.autor = autor
        self.ruta = ruta.strip()
        self.contenido = None
        self.lineas = self.definirContenido()

    def __str__(self) -> str:
        return (f"{self.titulo} ({self.autor})")
    
    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return (self.autor, self.titulo) == (other.autor, other.titulo)

    def __lt__(self, other):
        if not isinstance(other, Libro):
            return NotImplemented
        return (str(self.autor).lower(), self.titulo.lower()) < \
               (str(other.autor).lower(), other.titulo.lower())

    def definirContenido(self):
        rutaCompleta = os.path.join(rutaCarpetaContenidos, self.ruta)
        contador = 0
        try:
            if os.path.exists(rutaCompleta):
                with open(rutaCompleta, "r", encoding="utf-8") as ficheroContenido:
                    self.contenido = ficheroContenido.read()
                    if self.contenido.strip() == "":
                        return 0
                    return len(self.contenido.splitlines())
            else:
                with open(rutaCompleta, "w", encoding="utf-8") as ficheroContenido:
                    ficheroContenido.write("")
                self.contenido = ""
            return contador
        except FileNotFoundError:
            print(f"Error: La ruta del contenido del libro '{self.titulo}' no se ha podido encontrar.")
        except IOError:
            print(f"Error: Fallo en la conexión con la ruta del contenido del libro '{self.titulo}'.")
        except PermissionError:
            print(f"Error: No hay permisos suficientes para gestionar la ruta '{self.ruta}'.")
        except Exception as e:
            print(f"Error: {type(e)}")