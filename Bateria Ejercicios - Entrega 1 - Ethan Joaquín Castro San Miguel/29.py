"""
29. Realiza un programa que devuelva la cantidad de vocales, consonantes y espacios en
una cadena dada. Supondremos que no las vocales no estarán acentuadas.
"""

def Ejercicio29():
    cadena = input("Introduce una oración. Es importante que las vocales no estén acentuadas: ")
    consonantes = vocales = espacios
    vocal = "aeiou"
    espacio = " "
    for caracter in cadena:
        if caracter == espacio:
            espacios = espacios+1
        elif caracter in vocal:
            vocales = vocales+1
        elif caracter not in vocal and espacio:
            consonantes = consonantes+1
    print(f"En la oración dada hay un total de {vocales} vocales, {consonantes} consonantes y {espacios} espacios.")

Ejercicio29()