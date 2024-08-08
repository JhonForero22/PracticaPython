class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True
    
    def prestar(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True
    
    def mostrarInformacion(self):
        if self.disponible == True:
            estado = "Disponible"
            print(f"Titulo: {self.titulo}, Autor: {self.autor}, Año de Publicidad: {self.anio_publicacion}, Disponible: {estado}")
        else:
            estado = "Prestado"
            print(f"Titulo: {self.titulo}, Autor: {self.autor}, Año de Publicidad: {self.anio_publicacion}, Disponible: {estado}")