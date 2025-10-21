"""
13. Haz un programa en Java para jugar contra el ordenador a adivinar un número,
generado aleatoriamente (Math.random(), entre 1 y 200. El usuario debe introducir un
número por teclado y el programa le dirá mediante los símbolos '<' o '>', si el número
introducido es menor o mayor que el generado por el ordenador.

14. Finalmente, se mostrará un mensaje informando de cuantos intentos se han necesitado
para adivinar el número y si no se adivina se mostrará un mensaje diciendo que ha
perdido. El número máximo de intentos se pedirá por teclado.
"""

import random

def Ejercicio13y14():
    x = random.randint(1, 200)
    y = 0
    i = int(input("Introduce el máximo de intentos: "))
    while i != 0:
        y = int(input("Introduce un número: "))
        if y == x:
            print("Has adivinado el número. Bien chaval bien.")
            break
        elif y<x:
            print("<")
            i = i-1
        elif y>x:
            print(">")
            i = i-1
        if i == 0:
            print("Lo siento. Se han acabado los intentos. Has perdido.")
            break

Ejercicio13y14()