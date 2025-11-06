"""
2. Hacer un programa para sumar los N primeros términos de una progresión geométrica
de primer término A y razón R (dados por teclado). Se debe realizar la suma sin
emplear la fórmula que existe para ello. Muestra también los términos de la serie.
"""
def Ejercicio2():
    N = int(input("N: "))
    A = int(input("A: "))
    R = int(input("R: "))
    suma = 0
    for i in range (1, N+1):
        multiplicacion = A*R
        A = multiplicacion
        suma = suma+A
        print(A,", ",end='')
    print("\nLa suma es: ",suma)

Ejercicio2()