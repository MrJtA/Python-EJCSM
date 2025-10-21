"""
6. Hacer un programa que pida 2 números por teclado y calcule su división mediante
restas sucesivas. Imprimir su resultado. Divide siempre el más grande entre el más
pequeño.
"""

def Ejercicio6():
    x = int(input("Introduce de nuevo el dividendo: "))
    y = int(input("Introduce de nuevo el divisor: "))
    while x<y:
        print("Error: El dividendo debe ser mayor o igual que el divisor.")
        x = int(input("Introduce de nuevo el dividendo: "))
        y = int(input("Introduce de nuevo el divisor: "))
    resultado = 0
    while x>=y:
        x = x-y
        resultado = resultado+1
    print("El resultado de la división mediante restas sucesivas es: ",resultado)
    print("El resto es:",x)

Ejercicio6()