"""
30. Pedir un número entero y decir si es capicúa, es decir, por ejemplo: 1001 es capicúa.
"""

def Ejercicio30():
    x = int(input("Introduce un número: "))
    lista = []
    n = x
    if x>9:
        while x>0:
            unidad = x%10
            x = x//10
            lista.append(unidad)
        print(lista)
        if lista == list(reversed(lista)):
            print(f"El número {n} es capicúa")
        else:
            print(f"El número {n} no es capicúa")
    else:
        print("Al ser el número introducido un número de un solo digito, se podría decir que es capicúa.")

Ejercicio30()