def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Calcular potencia")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

def calcular_potencia():
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    resultado = pow(base, exponente)
    print(f"Resultado de {base} elevado a {exponente} es {resultado}")

def opcion_2():
    print("Has seleccionado la opción 2")

def opcion_3():
    print("Has seleccionado la opción 3")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            calcular_potencia()
        elif opcion == '2':
            opcion_2()
        elif opcion == '3':
            opcion_3()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()
