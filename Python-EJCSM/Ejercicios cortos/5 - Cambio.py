"""
Realiza un método que reciba un billete (o moneda) de euro (debe validarse que existe) y
devolverá la misma cantidad usando la mínima cantidad de billetes o monedas inferiores
necesarias.

denominacion = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1, 2, 500, 1000, 2000, 5000, 10000, 20000, 50000]

while True:
    cantidad = int(input("Introduce la cantidad: "))
    if cantidad in denominacion:
        break
    else:
        print("Introduce un billete o una moneda válida.")
        continue

def cambio(int cantidad) -> dict[float,int]:
    resultado = {}
    if cantidad in denominacion:
        for moneda in denominacion:
            if (cantidad>moneda):
                if cantidad%moneda == 0:
                    cantidadCambio = moneda
                    numeroMonedas = cantidad/moneda
                    resultado[cantidadCambio] = numeroMonedas
    return resultado

cambio(cantidad)

"""