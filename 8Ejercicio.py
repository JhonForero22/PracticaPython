"""
Este programa pide primeramente la cantidad total de compras de una persona.
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción.
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa 
genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un
color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente
recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno 
de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  
aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente 
el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento
"""

""" #Generar un numero random
x = random.randint(0,100)
"""

import random

#Información de la promocion
def promocion(): 
    print("")
    print("SU GASTO IGUALA O SUPERA LOS $100.00 Y POR TANTO PARTICIPA EN LA PROMOCION.")
    print("")
    print("  COLOR    DESCUENTO")
    print("")
    print("  BOLA BLANCA     NO TIENE")
    print("  BOLA ROJA       10 POR CIENTO")
    print("  BOLA AZUL       20 POR CIENTO")
    print("  BOLA VERDE      25 POR CIENTO")
    print("  BOLA AMARILLA   50 POR CIENTO")

#Calculo del random
def calculo(valor):
    descuento = 0
    x = random.choice([0, 10, 20, 25, 50])
    
    bolas = {0:"BOLA BLANCA",
         10:"BOLA ROJA",
         20:"BOLA AZUL",
         25:"BOLA VERDE",
         50:"BOLA AMARILLA"}

    if x == 0:
        print("ALEATORIAMENTE USTED OBTUVO UNA BOLA BLANCA")
        print("")
        print("LAMENTABLEMENTE EN ESTA OPORTUNIDAD NO HAY DESCUENTO")
    else:
        print("ALEATORIAMENTE USTED OVTUVO UNA", bolas[x])
        print("")
        print("FELICIDADES, HA GANADO UN", x, "POR CIENTO DE DESCUENTO")
        print("")
        print("SU NUEVO TOTAL A PAGAR ES: $", float (valor -(float(valor * x)/100)))
        print("")

#Funcion principal
def compras(): 
    valor_compra = input("INTRODUZCA LA CANTIDAD TOTAL DE LA COMPRA: ")
    valor_compra = int(valor_compra)
    if valor_compra < 100:
        print("")
        print("El cliente no aplica la promocion!!!")
    else:
        promocion()
        calculo(valor_compra)

compras()