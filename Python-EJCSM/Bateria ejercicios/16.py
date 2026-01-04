"""
16. Haz un programa que muestre un contador con 3 dígitos. Mostrará los números del 0-
0-0 al 9-9-9, cada vez que aparezca un 3 lo sustituiremos por una E.
"""

def Ejercicio16():
    for i in range(1000):
        unidad = i%10
        decena = (i//10)%10
        centena = i//100
        centena = "E" if centena == 3 else centena
        decena = "E" if decena == 3 else decena
        unidad = "E" if unidad == 3 else unidad
        print(f"{centena}-{decena}-{unidad}")

Ejercicio16()