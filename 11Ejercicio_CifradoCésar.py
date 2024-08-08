"""
Ejercicio: Cifrado César
El Cifrado César es una técnica de cifrado simple en la que cada letra de un 
texto se desplaza un número fijo de posiciones en el alfabeto. Por ejemplo, 
con un desplazamiento de 3, la letra "A" se convierte en "D", "B" en "E", y 
así sucesivamente. Si llegamos al final del alfabeto, volvemos al principio,
por ejemplo, "Z" se convierte en "C".

Instrucciones
Escribe una función en Python llamada cifrado_cesar que tome dos argumentos:

texto: una cadena de texto que representa el mensaje a cifrar.
desplazamiento: un entero que representa el número de posiciones a desplazar
en el alfabeto.
La función debe devolver una nueva cadena que sea el texto cifrado.

Asegúrate de que la función maneje tanto letras mayúsculas como minúsculas 
y que otros caracteres (como espacios, números y signos de puntuación) se 
mantengan sin cambios.

Pistas
Puedes utilizar la función ord() para obtener el código ASCII de un 
carácter y chr() para convertir un código ASCII en un carácter.
Recuerda manejar tanto mayúsculas como minúsculas por separado.
Considera el uso del operador módulo (%) para hacer el desplazamiento 
circular dentro del alfabeto.

"""

def cifrado_cesar(entrada, desplazamiento):
    resultado = []
    for caracter in entrada:
        if caracter.isalpha():
            # Determina si es mayúscula o minúscula
            offset = 65 if caracter.isupper() else 97
            
            # Aplica el desplazamiento dentro del rango de letras
            nuevo_caracter = chr((ord(caracter) - offset + desplazamiento) % 26 + offset)
            resultado.append(nuevo_caracter)
        else:
            # Mantén caracteres no alfabéticos sin cambios
            resultado.append(caracter)
    
    # Une la lista en una cadena y la retorna
    return ''.join(resultado)

# Ejemplo 1
entrada = "Hola Mundo"
desplazamiento = 3
salida = cifrado_cesar(entrada, desplazamiento)
print(salida)  # Salida esperada: "Krod Pxqgr"

# Ejemplo 2
entrada = "Python 3.8!"
desplazamiento = 5
salida = cifrado_cesar(entrada, desplazamiento)
print(salida)  # Salida esperada: "Udymts 3.8!"
