class Pokemon:

    def __init__(self, numero : int, nombre : str, descripcion : str):
        self.numero = numero
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return (f"{self.numero};{self.nombre};{self.descripcion}")

class Entrenador:

    def __init__(self, nombre : str, rutaBBDD : str):
        self.nombre = nombre
        self.rutaBBDD = rutaBBDD
        self.numeroTotalPokemon, self.numeroPokemonPokedex, self.pokedex = self.cargarPokemon()

    def cargarPokemon(self):
        pokedex = {}
        try:
            for i in range(1, 151):
                pokedex[i] = None
            with open(self.rutaBBDD, "r") as bbddPokemon:
                numeroTotalPokemon = 0
                for linea in bbddPokemon:
                    linea = linea.strip()
                    linea = linea.split(";")
                    numero = int(linea[0])
                    nombre = linea[1]
                    descripcion = linea[2]
                    pokemon = Pokemon(numero, nombre, descripcion)
                    pokedex[numero] = pokemon
                    numeroTotalPokemon += 1
                numeroPokemonPokedex = len(pokedex)
            return numeroTotalPokemon, numeroPokemonPokedex, pokedex
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los pokemon del entrenador no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la ruta de la base de datos del entrenador.")
        except Exception as e:
            print("Error: ", type(e))

    def actualizarPokemon(self, pokemon : Pokemon):
        try:
            with open(self.rutaBBDD, "a") as bbddPokemon:
                bbddPokemon.write(str(pokemon))
                bbddPokemon.write("\n")
            self.numeroTotalPokemon += 1
            self.pokedex[pokemon.numero] = pokemon
            self.numeroPokemonPokedex = len(self.pokedex)
            return True
        except FileNotFoundError:
            print("Error: La ruta de la base de datos de los pokemon del entrenador no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la ruta de la base de datos del entrenador.")
        except Exception as e:
            print("Error: ", type(e))
        return False


class Pokedex:

    def __init__(self, ruta : str):
        self.ruta = ruta
        self.pokedex = self.crearPokedex()

    def crearPokedex(self):
        pokedex = {}
        try:
            with open(self.ruta, "r", encoding="utf-8") as rutaPokedex:
                for linea in rutaPokedex:
                    linea = linea.strip()
                    linea = linea.split(";")
                    numero = int(linea[0])
                    nombre = linea[1]
                    descripcion = linea[2]
                    pokemon = Pokemon(numero, nombre, descripcion)
                    pokedex[numero] = pokemon
            return pokedex
        except FileNotFoundError:
            print("Error: La ruta de la pokedex de los libros no se ha podido encontrar.")
        except IOError:
            print("Error: Fallo en la conexión con la ruta de la pokedex.")
        except Exception as e:
            print(f"Error: {type(e)}")