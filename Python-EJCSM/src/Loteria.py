"""
Crear un programa de loteria.
El programa creara automaticamente un boleto ganador
de 4 numeros del 1 al 99.
Al iniciarse te dara las siguientes opciones.
- Comprar boleto.
- Ver boletos comprados.
- Probar suerte con un boleto.
	- tienes X boletos, cual quieres comprobar?
	(Lo borra)
- Probar todos los boletos
- Salir
"""

import random

winner = [random.randint(1, 99) for i in range(4)]
boletos = []
txt = "--------------------"
txt += '\n1 > Compra tu boleto !\n2 > Ver mis boletos\n3 > Comprobar un boleto\n4 > Comprobar todos los boletos\n5 > Salir'
txt += "\n--------------------\n"

while True:
    n = int(input(txt))
    print()
    match n:
        case 1:
            #boleto = [random.randint(1, 99) for _ in range(4)]
            boleto = []
            for i in range(4):
                num = random.randint(1,1)
                boleto.append(num)
            boletos.append(boleto)
        case 2:
            for b in boletos:
                print(b)
        case 3:
            elegido = int(input(f"Tienes {len(boletos)}. ¿Cual quieres comprobar?"))
            if len(boletos) > elegido >= 0:
                ganador = True
                for j in range(4):
                    if winner[j] != boletos[elegido][j]:
                        ganador = False
                #boletos.pop(elegido)
                del boletos[elegido]
                if ganador:
                    print("Enhorabuena, has ganado la loteria!!!!!!!!")
                else:
                    print("Sigue probando")

        case 4:
            if winner in boletos:
                print("Enhorabuena, has ganado la loteria!!!!!!!!")
            else:
                print("Sigue probando")

        case 5:
            break
