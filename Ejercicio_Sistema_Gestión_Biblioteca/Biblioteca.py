class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
    
    def prestarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.disponible:
                    libro.prestar()
                    print(f"El libro '{titulo}' ha sido prestado.")
                else:
                    print(f"El libro '{titulo}' no está disponible.")
        print(f"El libro: {titulo} no se encuentra en la Biblioteca")

    def devolverLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                libro.devolver()
                print(f"El libro '{titulo}' ha sido devuelto.")
                return
        print(f"El libro '{titulo}' no se encontró en la biblioteca.")
    
    def mostrarLibro(self):
        print(f"Biblioteca: {self.nombre}")
        if not self.libros:
            print("No hay libros en la biblioteca")
        else:
            for libro in self.libros:
                libro.mostrarInformacion()