'''
Crear una función llamada menu()
Parametros de entrada: Nunguno
Lo que realiza: Muestra un menu y pide al usuario que seleccione una opción
Valor de retorno: La opción seleccionada
'''
def menu():
    print("1. Entradas\n2. Platos Fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opción: "))
    return opcion

def entradas():
    print("1. Pan de bono\t\t$3000")
    print("2. Empanada\t\t$3500")

def fuertes():
    print("Bandeja Paisa\t\t$15000")
    print("Pasta con Cosas\t\t$21000")
    print("Caviar\t\t\t$495000")

def bebidas():
    print("Manzana Postobon\t$3500")
    print("Jugo de Mango\t\t$2800")
    print("Botella de Agua\t\t$3200")

def postres():
    print("Helado de Chocolate\t$3000")
    print("Tarta de Almendras\t$6000")


# Funcion principal
eleccion = menu()
print(eleccion)

match eleccion:
    case 1:
        entradas()
    case 2:
        fuertes()
    case 3:
        bebidas()
    case 4:
        postres()
    case _:
        print("Opcion no valida.")
