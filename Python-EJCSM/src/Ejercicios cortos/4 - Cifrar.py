"""
Realiza un método que reciba una palabra y una tabla.
La tabla contendrá dos filas, la primera con las letras del abecedario, y la segunda con su
equivalencia cifrada, la cual usaremos para cifrar la palabra recibida.
Devolver la palabra inicial cifrada.
Ej
| A | B | C | D | E | ....
| J | X | A | N | W | ...
"""

import random
import string

palabra = input("Introduce una palabra: ")
lista = []

for i in range(2):
    aux = []
    for letra in string.ascii_uppercase:
        aux.append(letra)
    if i == 1:
        random.shuffle(aux)
    lista.append(aux)

print(lista[0])
print(lista[1])

def cifrar(palabra : str, tabla : list[list[str]]) -> str:
    abc = tabla[0]
    cifrado = tabla[1]
    palabraCifrada = ""
    for caracter in palabra:
        posicion = abc.index(caracter)
        nuevoCaracter = cifrado[posicion]
        palabraCifrada = palabraCifrada+nuevoCaracter
    return palabraCifrada

palabraCifrada = cifrar(palabra, lista)
print(f"La palabra cifrada es: {palabraCifrada}")