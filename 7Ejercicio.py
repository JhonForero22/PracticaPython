"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def funcionMax(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
print(funcionMax(185,7))
"""

"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y 
multip([1,2,3,4]) debería devolver 24


def sum(num1,num2,num3,num4):
    return num1 + num2 + num3 + num4

def multip(num1,num2,num3,num4):
    return num1 * num2 * num3 * num4

print(sum(1,2,3,4))
print(multip(1,2,3,4))
"""

"""
Definir una función inversa() que calcule la inversión de una cadena.
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
def inversa(letras):
    listLetrasAlReves = []
    #Proceso para ir de la ultima letra a la primera
    for letra in letras[::-1]:
        listLetrasAlReves.append(letra)

    #Proceso para convertir una lista en texto usando join
    textoAlReves = ''.join(listLetrasAlReves)    
    #Imprimir
    print(textoAlReves)
    
inversa("Hola Mundo")