"""
28. Haz un programa que pida un número, entre 0 y 10, y escriba un triángulo invertido
con dichos números. Por ejemplo, si n=10:
0,1,2,3,4,5,6,7,8,9
1,2,3,4,5,6,7,8,9
2,3,4,5,6,7,8,9
3,4,5,6,7,8,9
4,5,6,7,8,9
5,6,7,8,9
6,7,8,9
7,8,9
8,9
9
"""

def Ejercicio28():
    lista = []
    n = int(input("Introduce la altura: "))
    for i in range(n+1):
        lista.append(i)
    for i in range(n+1):
        print(lista)
        lista.pop(0)

Ejercicio28()