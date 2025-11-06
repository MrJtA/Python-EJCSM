"""
27. Realiza un programa que pinte la letra U por pantalla hecha con asteriscos. El
programa pedirá la altura.
"""

def Ejercicio27():
    a = int(input("Introduce la altura: "))
    asterisco = "*"
    base = " * * * "
    for i in range(a-1):
        print(asterisco,"   ",asterisco)
    print(base)

Ejercicio27()