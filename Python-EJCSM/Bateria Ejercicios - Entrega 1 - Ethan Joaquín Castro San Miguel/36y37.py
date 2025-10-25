"""
36. Dada una cadena, devolver la mitad de esta.

37. Modificar el programa anterior para que nos permita elegir si queremos obtener la
mitad izquierda o derecha.
"""

def Ejercicio36y37():
    cadena = input("Introduce una cadena de texto: ")
    opcion = 0
    while not opcion == 1 or opcion == 2:
        opcion = int(input("Introduzca 1 para mostrar la mitad izquiera, o 2 para mostrar la mitad derecha: "))
        if opcion == 1:
            for i in range((len(cadena))//2):
                print(cadena[i], end="")
        elif opcion == 2:
            for i in range((len(cadena))//2):
                print(cadena[((len(cadena))//2)+i], end="")
    

Ejercicio36y37()