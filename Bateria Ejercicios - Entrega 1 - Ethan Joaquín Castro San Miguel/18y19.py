"""
18. Para obtener el número del tarot de una persona, hay que sumar los números de su
fecha de nacimiento y reducirlo a un solo dígito. Ejemplo de Julio de 1980 sería igual
a: 1+7+1980 = 1988 → 1+9+8+8 = 26 → 2+6=8, por lo tanto, el número del tarot
sería el 8.

19. Realiza un programa que pida una fecha de nacimiento por teclado (elige el formato
que creas adecuado) y escriba el número del tarot, prueba con la edad de tus
compañeros.
"""

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

Ejercicio18y19()