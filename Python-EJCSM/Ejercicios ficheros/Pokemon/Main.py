from Clases import Entrenador
from Clases import Pokedex
import random

pokedex = Pokedex("pokedex.txt")
entrenador = Entrenador("Joaco", "misPokemon.txt")

def pedirOpcion():
    while True:
        try:
            opcion = int(input("Introduce una opción: "))
            return opcion
        except ValueError:
            print("Error: Introduce un valor válido.")

def atraparPokemon():
    numero = random.randint(1, 151)
    pokemon = None
    pokemonRepetido = False
    for k, v in pokedex.pokedex.items():
        if numero == k:
            pokemon = v
    print(f"¡Un {pokemon.nombre} salvaje ha aparecido!")
    if entrenador.pokedex[pokemon.numero] is None:
        print("No tienes capturado a este pokémon.")
    else:
        print("Ya tienes a este pokémon.")
        pokemonRepetido = True
    oportunidades = 0
    while True:
        print("1. Lanzar Pokéball.")
        print("2. Huir.")
        opcion = pedirOpcion()
        match opcion:
            case 1:
                acierto = random.randint(0,1)
                if acierto == 0:
                    print("El pokémon se ha escapado.")
                    oportunidades += 1
                    if oportunidades == 3:
                        print(f"El {pokemon.nombre} se ha escapado.")
                        break
                else:
                    if entrenador.actualizarPokemon(pokemon):
                        print(f"¡Has atrapado a {pokemon.nombre}!")
                        if not pokemonRepetido:
                            print("Añadido a la pokedex")
                            print(f"Nombre: {pokemon.nombre}")
                            print(f"Número: # {pokemon.numero}")
                            print(f"Descripción: {pokemon.descripcion}")
                    break
            case 2:
                break
            case _:
                print("Introduce una opción válida por favor.")

def verPokedex():
    print("- Pokédex -")
    for k, v in entrenador.pokedex.items():
        if v is None:
            print(f"# {k} - ???")
        else:
            print(f"# {k} - {v.nombre}: {v.descripcion}")

def menu():
    while True:
        print("- Pokémon -")
        print("0. Salir.")
        print("1. Atrapar pokémon.")
        print("2. Ver pokédex.")
        opcion = pedirOpcion()
        match opcion:
            case 0:
                break
            case 1:
                atraparPokemon()
            case 2:
                verPokedex()
            case _:
                print("Introduce una opción válida por favor.")

menu()