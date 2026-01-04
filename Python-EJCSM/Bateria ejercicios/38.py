"""
38. Dada una cadena, reemplaza todas las letras a por una e y devuelve cuantas letras
has reemplazado.
"""

def Ejercicio38():
    cadena = input("Introduce una cadena de texto: ")
    contador = 0
    for caracter in cadena:
        if caracter == "a":
            caracter = "e"
            contador = contador+1
        print(caracter,end="")
    print(f"\nSe han remplazado todas las 'a' por una 'e', un total de {contador} veces")

Ejercicio38()