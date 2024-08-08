"""
Arrays:
Los arrays (o arreglos) en Python son una estructura de datos que permiten
almacenar elementos del mismo tipo en una secuencia ordenada
Solo pueden contener elementos del mismo tipo
"""

"""
2. Creación de Arrays

import array
# Crear un array de enteros (tipo 'i' es para enteros)
mi_array = array.array('i', [1, 2, 3, 4, 5])
print(mi_array)
"""

"""
3. Tipos de Datos en Arrays
'b': Enteros con signo de 1 byte (8 bits).
'B': Enteros sin signo de 1 byte.
'i': Enteros con signo de 2 bytes (16 bits).
'I': Enteros sin signo de 2 bytes.
'f': Números de punto flotante de 4 bytes (32 bits).
'd': Números de punto flotante de 8 bytes (64 bits)
mi_array = array.array('f', [1.5, 2.7, 3.1, 4.0])
"""

"""
4. Operaciones Básicas con Arrays
print(mi_array[2])  # Imprime 3.1, Acceder a elementos

mi_array[1] = 5.5 # Modificar elementos
print(mi_array)  # Imprime array('f', [1.5, 5.5, 3.1, 4.0])

mi_array.append(6.2) #Añadir elementos al final
mi_array.remove(3.1) #Eliminar elementos
longitud = len(mi_array) #Obtener la longitud
"""

"""
5. Arrays Multidimensionales
import numpy as np
# Crear un array de 2D (matriz)
mi_matriz = np.array([[1, 2, 3], [4, 5, 6]])
"""

