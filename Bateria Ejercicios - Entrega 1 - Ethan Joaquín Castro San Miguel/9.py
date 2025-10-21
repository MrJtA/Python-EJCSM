"""
9. Escribir un programa que imprima cada uno de los términos de la serie 2, 5, 7, 10, 12,
15, 17,..., 1800. Además, calcule e imprima la suma de los términos.
"""

def Ejercicio9():
    contador = suma = total = 0
    while suma!=1800:
        if contador%2 == 0:
            suma = suma+2
            total = total+suma
        else:
            suma = suma+3
            total = total+suma
        print(suma)
        contador = contador+1
    print("La suma total de todos los números anteriores es: " + total)
    
Ejercicio9()