"""
7. Haz un programa que lea un número entero N y calcule el resultado de la siguiente
serie: 1+1/2+1/3+1/4+1/5+...+1/N.
"""

def Ejercicio7():
    N = int(input("N: "))
    suma = 0.0
    for i in range (1, N+1):
        operacion = 1/i
        suma = suma+operacion
    print("El resultado de la suma es: ",suma)

Ejercicio7()