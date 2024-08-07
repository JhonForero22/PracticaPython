class Persona:
    #Constructor
    def __init__(self ,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumplir_anios(self):
        self.edad += 1
        
    def mostrar_informacion(self):
        # f-string (cadena formateada)
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
#Crear Persona
persona1 = Persona("Jhon",21)

#Imprimir
persona1.mostrar_informacion()

#Cumple años la persona
persona1.cumplir_anios()

#Imprimir de nuevo
persona1.mostrar_informacion()