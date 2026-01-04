from Clases import *
# personas de prueba
p1 = Persona('Juan', 'Carlos', 1)
p2 = Persona('Jair', 'Cedeño', 2)
p3 = Persona('Alejandro', 'Jimenez', 3)
p4 = Persona('Jolina', 'Jimenez', 4)
p5 = Persona('Daniel', 'Perez', 5)
p6 = Persona('Carlos', 'Domingo', 6)

# fechas de prueba
f1 = Fecha(1, 5, 2000)
f2 = Fecha(7, 3, 2004)
f3 = Fecha(11, 2, 1996)
f4 = Fecha(1, 5, 1980)
f5 = Fecha(11, 2, 2003)
f6 = Fecha(21, 8, 1998)

# diccionario ya creado
diccionario1 = {p1 : f1, p2 : f2, p3 : f3,
                p4 : f4, p5 : f5, p6 : f6}

# diccionario desde 0
diccionario2 = {}
diccionario2[p1] = f1
diccionario2[p2] = f2
diccionario2[p3] = f3
diccionario2[p4] = f4
diccionario2[p5] = f5
diccionario2[p6] = f6

# recorro el diccionario
for k, v in diccionario1.items():
    print(f'key : {k}, value : {v}')


# 1. True si hay gente que cumple el mismo dia
dia = int(input('Introduce un dia: '))

contador = 0
for fecha in diccionario1.values():
    if fecha.dia == dia:
        contador += 1
if contador > 1:
    print(f'Existen {contador} personas que cumple el dia {dia}')


# 1. Mostrar tambien el dni de esas personas
for persona, cumple in diccionario1.items():
    if cumple.dia == dia:
        print(f'Su dni es : {persona.dni} y se apellida {persona.apellido}')

# 2. Introducir un mes y listar los cumpleañeros
mes = int(input('Introduce un mes: '))

for persona, cumple in diccionario1.items():
    if cumple.mes == mes:
        print(persona)