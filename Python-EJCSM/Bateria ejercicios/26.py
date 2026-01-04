"""
26. Muestra 50 números enteros aleatorios entre 100 y 199 (ambos incluidos) separados
por espacios. Muestra también el máximo, el mínimo y la media de esos números.
"""

def Ejercicio26():
    max = suma = 0
    min = 200
    print("Los 50 números aleatorios generados entre el 100 y 199 son: ", end="")
    for i in range(1, 51):
        x = random.randint(100, 199)
        print(x, end=" ")
        if x>max:
            max = x
        if x<min:
            min = x
        suma = suma+x
    print(f"\nEl número más grande ha sido el {max}, el más pequeño el {min}, y la media es igual a {suma/50}")

Ejercicio26()