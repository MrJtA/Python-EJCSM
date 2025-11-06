"""
33. Dadas dos fechas, mostrar el número de días que hay de diferencia. Para una mayor
comodidad, supondremos que todos los meses tienen 30 días.
"""

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

Ejercicio33()