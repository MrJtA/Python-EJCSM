"""
17. Modificar el programa anterior para que la cantidad de dígitos del contador venga
dada por el usuario.
"""

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

Ejercicio17()