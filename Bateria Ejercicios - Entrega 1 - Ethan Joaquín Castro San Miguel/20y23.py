"""
20. Realiza un programa que pida números hasta que se introduzca cero o un número
negativo, tras esto, se deberá mostrar la cantidad de números introducidos.

23. Realiza un programa que pida números hasta que se introduzca cero o un número
negativo, y diga cuál es el mayor número introducido y cuantas veces se repite.
"""

def Ejercicio20y23():
    x = 1
    max = 0
    lista = []
    while x>0:
        x = int(input("Introduce un número: "))
        lista.append(x)
        if x>max:
            max = x
    lista.pop()
    print(f"Los números que se han introducido hasta que se ha introducido uno igual o menor que cero son los siguientes: {lista}. Son un total de {len(lista)}. El número más grande introducido ha sido el {max}, y se repite un total de {lista.count(max)} veces.")

Ejercicio20y23()