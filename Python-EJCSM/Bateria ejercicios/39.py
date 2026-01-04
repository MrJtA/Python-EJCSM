"""
39. Realiza una calculadora que nos pida dos operandos enteros y un signo matemático.
Tras realizar la operación indicada, nos deberá mostrar el resultado. Las operaciones
soportadas son: +, -, *, /, ^ (potencia, primer operando base y segundo exponente) y
%.
"""

def Ejercicio39():
    x = int(input("Introduce el primer operando entero: "))
    operacion = input("Introduce el signo de la operación que quieres realizar, siendo los disponibles: +, -, *, /, ^ (potencia) y % (resto de una división): ")
    y = int(input("Introduce el segundo operando entero: "))
    if operacion == "+":
        print("El resultado es: ",x+y)
    elif operacion == "-":
        print("El resultado es: ",x-y)
    elif operacion == "*":
        print("El resultado es: ",x*y)
    elif operacion == "/":
        print("El resultado es: ",x/y)
    elif operacion == "^":
        print("El resultado es: ",x**y)
    elif operacion == "%":
        print("El resultado es: ",x%y)
    else:
        print("Operación no válida.")

Ejercicio39()