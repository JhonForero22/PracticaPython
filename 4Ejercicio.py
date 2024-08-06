"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def totalFactura(cantidad, iva=21):
    return cantidad * iva/100 + cantidad
   
print("El total de la factura es: " + str(totalFactura(5000,10)))
print("El total de la factura es: " + str(totalFactura(5000)))