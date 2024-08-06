"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
        Renta               Tipo impositivo
    Menos de 10000€	            5%
    Entre 10000€ y 20000€	    15%
    Entre 20000€ y 35000€	    20%
    Entre 35000€ y 60000€	    30%
    Más de 60000€	            45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
rentaAnual = int(input("Ingrese su renta anual: "))
if (rentaAnual < 10000):
    print("El tipo impositivo que le corresponde es igual a " + str(rentaAnual * 5 / 100) + ", para un total " + str(rentaAnual * 5 / 100 + rentaAnual) )
elif (rentaAnual >= 10000 and rentaAnual < 20000):
    print("El tipo impositivo que le corresponde es igual a " + str(rentaAnual * 15 / 100) + ", para un total " + str(rentaAnual * 5 / 100 + rentaAnual) ) 
elif (rentaAnual >= 20000 and rentaAnual < 35000):
    print("El tipo impositivo que le corresponde es igual a " + str(rentaAnual * 20 / 100) + ", para un total " + str(rentaAnual * 5 / 100 + rentaAnual) )
elif (rentaAnual >= 35000 and rentaAnual < 60000):
    print("El tipo impositivo que le corresponde es igual a " + str(rentaAnual * 30 / 100) + ", para un total " + str(rentaAnual * 5 / 100 + rentaAnual) )
elif (rentaAnual > 60000):
    print("El tipo impositivo que le corresponde es igual a " + str(rentaAnual * 45 / 100) + ", para un total " + str(rentaAnual * 5 / 100 + rentaAnual) )
else:
    print("Valor fuera de rango!!!")