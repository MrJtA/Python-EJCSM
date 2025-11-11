"""
Escribe un programa que combine dos diccionarios. Si alguna clave está repetida, la clave
del segundo diccionario debe sobrescribir la del primero.
No debe usarse un tercer diccionario, sino combinar el segundo en el primero.
"""

import random

a = {}
b = {}

for i in range(10):
    clave = random.randint(1,10)
    valor = random.randint(1,10)
    a[clave] = valor

for i in range(10):
    clave = random.randint(1,10)
    valor = random.randint(1,10)
    b[clave] = valor

print(a)
print(b)

for kb, vb in b.items():
    a[kb] = vb

print(a)