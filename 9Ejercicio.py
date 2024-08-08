"""
Este programa muestra primero el listado de categorías de películas y pide al usuario
que introduzca el código de la categoría de la película y posterior a ello pide que 
el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.
"""

precio = [2.50, 3.00, 3.50, 4.00]
recargoDia = [0.50, 0.75, 1.00, 1.50]

def menuCine():
    print("     CATEGORIA       PRECIO      CODIGO      RECARGO/DIA DE ATRASO")
    print("")
    print("     FAVORITOS       $2.50          1                $0.50")
    print("     NUEVOS          $3.00          2                $0.75")
    print("     ESTRENOS        $3.50          3                $1.00")
    print("     SUPER ESTRENOS  $4.00          4                $1.50")
    print("")
    numCodigo = int(input("INTRODUZCA EL CODIGO DE LA CATEGORIA DE LA PELICULA: "))
    numDias = int(input("INTRODUZCA EL NUMERO DE DIAS DE ATRASO EN LA DEVOLUCION: "))
    totalPagar(numCodigo, numDias)
    
def totalPagar(codigo, dias):    
    if codigo == 1:
        print("EL TOTAL A PAGAR ES: $", float(precio[codigo-1] + (recargoDia[codigo-1] * dias)))
    elif codigo == 2:
        print("EL TOTAL A PAGAR ES: $", float(precio[codigo-1] + (recargoDia[codigo-1] * dias)))
    elif codigo == 3:
        print("EL TOTAL A PAGAR ES: $", float(precio[codigo-1] + (recargoDia[codigo-1] * dias)))
    elif codigo == 4:
        print("EL TOTAL A PAGAR ES: $", float(precio[codigo-1] + (recargoDia[codigo-1] * dias)))
    else:
        print("CODIGO NO VALIDO")
        
menuCine()