"""
34. Realizar un programa que muestre el producto de los N primeros números impares.
"""

def Ejercicio34():
    producto = 1
    N = int(input("N: "))
    for i in range(1, N+1):
        if i%2 != 0:
            impar = i
            print(impar)
            producto = producto*impar
    print(f"El producto de los {N} primeros números impares es: {producto}")

Ejercicio34()