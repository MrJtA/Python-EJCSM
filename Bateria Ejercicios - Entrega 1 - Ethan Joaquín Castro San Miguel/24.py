"""
24. Haz un programa que pida un número n, y diga cuantos y cuales números primos hay
entre 1 y n.
"""

def Ejercicio24():
    n = 0
    while n<1:
        n = int(input("Introduce un número: "))
    lista = []
    for i in range(2, n+1):
        noesPrimo = False
        for j in range (2, i):
            if i%j == 0:
                noesPrimo = True
        if noesPrimo == False:
            lista.append(i)
    print(f"Entre 1 y {n}, hay un total de {len(lista)} números primos, los cuales son: {lista}.")


Ejercicio24()