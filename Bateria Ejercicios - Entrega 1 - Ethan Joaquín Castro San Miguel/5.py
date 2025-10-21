"""
5. Haz un programa que pida 2 números por teclado y calcule su producto mediante
sumas sucesivas. Imprimir su resultado.
"""

def Ejercicio5():
    x = int(input("Introduce el primer número: "))
    y = int(input("Introduce el segundo número: "))
    suma = 0
    for i in range(y):
        suma = suma+x
    print("El resultado del producto mediante sumas sucesivas es: ",suma)

Ejercicio5()