"""
Listas (list)
Descripción: Una lista es una colección ordenada de elementos que pueden 
ser de diferentes tipos de datos. Las listas son mutables.

mi_lista = [1, 2, 3, "cuatro", 5.0]
# Operaciones comunes:
mi_lista.append(6)  # Añadir un elemento
mi_lista[1] = "dos"  # Modificar un elemento
del mi_lista[3]  # Eliminar un elemento
mi_lista.reverse() # Colocar lista al reves
print(mi_lista)
"""

"""
Tuplas (tuple)
Descripción: Una tupla es similar a una lista, pero es inmutable

mi_tupla = (1, 2, 3, "cuatro", 5.0)
elemento = mi_tupla[1]  # Acceder a un elemento
conteo = mi_tupla.count(2) # Devuelve el número de veces que value aparece en la tupla
indice = mi_tupla.index(2) # Devuelve el indice de la primera aparicion
indice = mi_tupla.index(2, 2) # Buscar el índice de 2 comenzando desde la posición 2
longitud = len(mi_tupla) # Devuelve la longitud de la tupla
maximo = max(mi_tupla) # Devuelve el elemento máximo 
minimo = min(mi_tupla) # Devuelve el elemento mínimo en la tupla
suma = sum(mi_tupla) # Devuelve la suma de los elementos
# in: Puedes usar el operador in para verificar si un elemento está presente en la tupla.
existe = 3 in mi_tupla  # Devuelve True si 3 está en la tupla
"""

"""
Conjuntos (set)
Descripción: Un conjunto es una colección desordenada de elementos únicos.
Es mutable y no permite duplicados

mi_conjunto = {1, 2, 3, 4, 5}
mi_conjunto.add(6)  # Añadir un elemento
mi_conjunto.remove(3)  # Eliminar un elemento
"""

'''
Diccionarios (dict)
Descripción: Un diccionario es una colección de pares clave-valor.
Es mutable, y las claves deben ser únicas e inmutables

mi_dict = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
mi_dict["edad"] = 31  # Modificar un valor
mi_dict["profesión"] = "Ingeniero"  # Añadir un nuevo par clave-valor
del mi_dict["ciudad"]  # Eliminar un par clave-valor
'''

"""
Listas por comprensión (List Comprehension)
Descripción: Una manera concisa y eficiente de crear listas a partir de secuencias existentes.

cuadrados = [x**2 for x in range(10)]

Puede incluir condiciones.
Ejemplo:
pares = [x for x in range(10) if x % 2 == 0]
"""

"""
Diccionarios por comprensión (Dict Comprehension)
Descripción: Similar a las listas por comprensión, pero para crear diccionarios.
cuadrado_dict = {x: x**2 for x in range(5)} #Sintaxis
mi_dict = {x: x*2 for x in range(5)} #Ejemplo
"""

"""
Pilas y Colas (con listas o collections.deque)
Pilas:
Implementadas usando listas, donde se añade y se elimina elementos
en el final de la lista (LIFO - Last In, First Out)
pila = []
pila.append(1)  # Push
pila.pop()  # Pop

Colas:
Implementadas usando listas o collections.deque, donde se añade al final
y se elimina del principio de la lista (FIFO - First In, First Out).
from collections import deque
cola = deque()
cola.append(1)  # Enqueue
cola.popleft()  # Dequeue
"""