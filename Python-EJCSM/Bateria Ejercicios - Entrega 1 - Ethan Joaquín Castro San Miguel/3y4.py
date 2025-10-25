"""
3. Haz un programa que dado un número N nos diga si es o no perfecto. Se dice que un
número N es perfecto si la suma de sus divisores, excluido el propio número es N. Por
ejemplo, 28 es perfecto, pues sus divisores son: 1, 2, 4, 7 y 14 y su suma es
1+2+4+7+14=28.

4. Modifica el programa anterior, para siga pidiendo números, para comprobar si son
perfectos, mientras el número introducido sea distinto de cero.
"""

def Ejercicio3y4():
    N = None
    while N != 0:
        N = int(input("N: "))
        suma = 0
        print("Sus divisores son:")
        for i in range (1, N):
            if N%i == 0:
                print(i,", ",end='')
                suma = suma+i
        print("\nLa suma de los divisores es: ",suma)
        if suma == N:
            print("Por lo tanto, el número",N,"es perfecto.\n")
        else:
            print("Por lo tanto, el número",N,"no es perfecto.\n")

Ejercicio3y4()