class Coche:
    def __init__(self,marca,modelo,anio,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
    
    def conducir(self,km):
        self.kilometraje += km
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Kilometraje: {self.kilometraje}")

# Crea una instancia de la clase Coche con la marca "Toyota", el modelo "Corolla", el año 2010 y un kilometraje inicial de 100000.
nuevoCoche = Coche("Toyota", "Corolla", 2010, 100000)

# Muestra la información del coche usando el método mostrar_informacion.
nuevoCoche.mostrar_informacion()

# Conduce el coche por 150 kilómetros usando el método conducir.
nuevoCoche.conducir(150)

# Muestra nuevamente la información del coche para verificar que el kilometraje ha sido actualizado.
nuevoCoche.mostrar_informacion()
