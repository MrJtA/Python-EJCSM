import random

def Ejercicio1():
    n = 0
    while n<=2:
        n = int(input("Introduce un número: "))
        for i in range (2, n):
            if n%i == 0:
                print(int((n/i)),"*",i,", ",end='')

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

def Ejercicio5():
    x = int(input("Introduce el primer número: "))
    y = int(input("Introduce el segundo número: "))
    suma = 0
    for i in range(y):
        suma = suma+x
    print("El resultado del producto mediante sumas sucesivas es: ",suma)

def Ejercicio6():
    x = int(input("Introduce de nuevo el dividendo: "))
    y = int(input("Introduce de nuevo el divisor: "))
    while x<y:
        print("Error: El dividendo debe ser mayor o igual que el divisor.")
        x = int(input("Introduce de nuevo el dividendo: "))
        y = int(input("Introduce de nuevo el divisor: "))
    resultado = 0
    while x>=y:
        x = x-y
        resultado = resultado+1
    print("El resultado de la división mediante restas sucesivas es: ",resultado)
    print("El resto es:",x)

def Ejercicio7():
    N = int(input("N: "))
    suma = 0.0
    for i in range (1, N+1):
        operacion = 1/i
        suma = suma+operacion
    print("El resultado de la suma es: ",suma)

def Ejercicio8():
    N = int(input("N: "))
    suma = 0.0
    for i in range (1, N+1):
        operacion = 1/i
        if i%2 != 0:
            suma = suma+operacion
        else:
            suma = suma-operacion
    print("El resultado de la suma es: ",suma)

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

def Ejercicio10():
    N = int(input("N: "))
    cadena = ""
    for i in range(1, N+1):
        cadena = cadena+"*"
        print(cadena)

def Ejercicio11():
    N = int(input("N: "))
    for i in range(1, N+1):
        print()
        for j in range(1, i+1):
            print(j, end=" ")

def Ejercicio12():
    N = int(input("N: "))
    for i in range(1, N+1):
        print()
        for j in range(1, 4):
            print(i**j, end=" ")

def Ejercicio13y14():
    x = random.randint(1, 200)
    y = 0
    i = int(input("Introduce el máximo de intentos: "))
    while i != 0:
        y = int(input("Introduce un número: "))
        if y == x:
            print("Has adivinado el número. Bien chaval bien.")
            break
        elif y<x:
            print("<")
            i = i-1
        elif y>x:
            print(">")
            i = i-1
        if i == 0:
            print("Lo siento. Se han acabado los intentos. Has perdido.")
            break

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

def Ejercicio16():
    for i in range(1000):
        unidad = i%10
        decena = (i//10)%10
        centena = i//100
        centena = "E" if centena == 3 else centena
        decena = "E" if decena == 3 else decena
        unidad = "E" if unidad == 3 else unidad
        print(f"{centena}-{decena}-{unidad}")

def Ejercicio17():
    x = int(input("Hasta que numero quieres imprimir la serie : "))
    for i in range(x+1):
        unidad = i%10
        decena = (i//10)%10
        centena = i//100
        centena = "E" if centena == 3 else centena
        decena = "E" if decena == 3 else decena
        unidad = "E" if unidad == 3 else unidad
        print(f"{centena}-{decena}-{unidad}")

def Ejercicio18y19():
    dia = mes = año = 0
    while not 1 <= dia <= 31:
        dia = int(input("Introduce el día: "))
    while not 1 <= mes <= 12:
        mes = int(input("Introduce el mes (número): "))
    while año <= 0:
        año = int(input("Introduce el año: "))
    resultado = (dia+mes+año)%9
    x = resultado if resultado != 0 else 9
    print("Tu número tarot es: ",x)

def Ejercicio20y23():
    x = 1
    max = 0
    lista = []
    while x>0:
        x = int(input("Introduce un número: "))
        lista.append(x)
        if x>max:
            max = x
    lista.pop()
    print(f"Los números que se han introducido hasta que se ha introducido uno igual o menor que cero son los siguientes: {lista}. Son un total de {len(lista)}. El número más grande introducido ha sido el {max}, y se repite un total de {lista.count(max)} veces.")

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

def Ejercicio25():
    print("Los 20 números aleatorios generados entre el 0 y 10 son: ", end="")
    for i in range(1, 21):
        x = random.randint(0, 10)
        print(x, end=" ")
    print("\n")

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

def Ejercicio27():
    a = int(input("Introduce la altura: "))
    asterisco = "*"
    base = " * * * "
    for i in range(a-1):
        print(asterisco,"   ",asterisco)
    print(base)

def Ejercicio28():
    lista = []
    n = int(input("Introduce la altura: "))
    for i in range(n+1):
        lista.append(i)
    for i in range(n+1):
        print(lista)
        lista.pop(0)

def Ejercicio29():
    cadena = input("Introduce una oración. Es importante que las vocales no estén acentuadas: ")
    consonantes = vocales = espacios
    vocal = "aeiou"
    espacio = " "
    for caracter in cadena:
        if caracter == espacio:
            espacios = espacios+1
        elif caracter in vocal:
            vocales = vocales+1
        elif caracter not in vocal and espacio:
            consonantes = consonantes+1
    print(f"En la oración dada hay un total de {vocales} vocales, {consonantes} consonantes y {espacios} espacios.")

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

def Ejercicio31():
    listaPalos = ["picas", "corazones", "diamantes", "tréboles"]
    listaNumeros = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    palo = random.randint(0, len(listaPalos)-1)
    numero = random.randint(0, len(listaNumeros)-1)
    print(f"{listaNumeros[numero]} de {listaPalos[palo]}")

def Ejercicio32():
    listaPalos = ["oros", "copas", "espadas", "bastos"]
    listaNumeros = ["as", 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"]
    palo = random.randint(0, len(listaPalos)-1)
    numero = random.randint(0, len(listaNumeros)-1)
    print(f"{listaNumeros[numero]} de {listaPalos[palo]}")

def Ejercicio33():
    dia1 = dia2 = mes1 = mes2 = año1 = año2 = 0
    while not 1 <= dia1 <= 30 or not 1 <= mes1 <= 12 or año1 <=0:
        dia1= int(input("Introduce el primer dia: "))
        mes1= int(input("Introduce el primer mes (número): "))
        año1= int(input("Introduce el primer año: "))
    while not 1 <= dia2 <= 30 or not 1 <= mes2 <= 12 or año2 <=0:
        dia2= int(input("Introduce el segundo dia: "))
        mes2= int(input("Introduce el segundo mes (número): "))
        año2= int(input("Introduce el segundo año: "))
    if año1>año2:
        dia1, dia2 = dia2, dia1
        mes1, mes2 = mes2, mes1
        año1, año2 = año2, año1
    aux1 = (((año1+1)*365)-365)+(((mes1+1)*30)-30)+dia1
    aux2 = (((año2+1)*365)-365)+(((mes2+1)*30)-30)+dia2
    print(f"El número de días que hay de diferencia entre el {dia1} de {mes1} del {año1}, y el {dia2} de {mes2} del {año2}, es de {aux2-aux1} días.")

def Ejercicio34():
    producto = 1
    N = int(input("N: "))
    for i in range(1, N+1):
        if i%2 != 0:
            impar = i
            print(impar)
            producto = producto*impar
    print(f"El producto de los {N} primeros números impares es: {producto}")

def Ejercicio35():
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")
        print()

def Ejercicio36y37():
    cadena = input("Introduce una cadena de texto: ")
    opcion = 0
    while not opcion == 1 or opcion == 2:
        opcion = int(input("Introduzca 1 para mostrar la mitad izquiera, o 2 para mostrar la mitad derecha: "))
        if opcion == 1:
            for i in range((len(cadena))//2):
                print(cadena[i], end="")
        elif opcion == 2:
            for i in range((len(cadena))//2):
                print(cadena[((len(cadena))//2)+i], end="")

def Ejercicio38():
    cadena = input("Introduce una cadena de texto: ")
    contador = 0
    for caracter in cadena:
        if caracter == "a":
            caracter = "e"
            contador = contador+1
        print(caracter,end="")
    print(f"\nSe han remplazado todas las 'a' por una 'e', un total de {contador} veces")

def Ejercicio39():
    x = int(input("Introduce el primer operando entero: "))
    operacion = input("Introduce el signo de la operación que quieres realizar, siendo los disponibles: +, -, *, /, ^ (potencia) y % (resto de una división): ")
    y = int(input("Introduce el segundo operando entero: "))
    if operacion == "+":
        print("El resultado es: ",x+y)
    elif operacion == "-":
        print("El resultado es: ",x-y)
    elif operacion == "*":
        print("El resultado es: ",x*y)
    elif operacion == "/":
        print("El resultado es: ",x/y)
    elif operacion == "^":
        print("El resultado es: ",x**y)
    elif operacion == "%":
        print("El resultado es: ",x%y)
    else:
        print("Operación no válida.")