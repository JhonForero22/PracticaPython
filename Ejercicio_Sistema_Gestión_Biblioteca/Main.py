from Libro import Libro
from Biblioteca import Biblioteca 

# Crear instancias de Libro
libro1 = Libro("1984", "George Orwell", 1949)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

# Crear una instancia de Biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# Agregar libros a la biblioteca
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)

# Mostrar todos los libros en la biblioteca
biblioteca.mostrarLibro()

# Prestar un libro y mostrar nuevamente
biblioteca.prestarLibro("1984")
biblioteca.mostrarLibro()

# Devolver el libro y mostrar nuevamente
biblioteca.devolverLibro("1984")
biblioteca.mostrarLibro()