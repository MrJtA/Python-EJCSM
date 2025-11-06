"""
15. Haz un programa en Java que muestre si dos números son o no amigos. Los números
se pedirán por teclado. Dos números son amigos si la suma de los divisores del
primero es el número y viceversa, excluimos en la suma el propio número.
"""

def Ejercicio15():
    x = int(input("Introduce el primer número: "))
    y = int(input("Introduce el segundo número: "))
    suma = 0
    print("Los divisores del primer número son: ")
    for i in range(1, x+1):
        if x%i == 0:
            print(i, ", ", end=" ")
            suma = suma+i
    suma = suma-x
    print("\nLa suma de los divisores del primer número es: ", suma)
    if suma == y:
        print("La suma de los divisores del primer número es igual al segundo número, por lo que dichos números son amigos.")
    else:
        print("La suma de los divisores del primer número no es igual al segundo número, por lo que dichos números no son amigos.")

Ejercicio15()