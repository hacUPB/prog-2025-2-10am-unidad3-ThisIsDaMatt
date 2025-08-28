control = True

while True:
    print("======================")
    print("    Menú Principal   ")
    print("======================")
    print("A. Opción A")
    print("B. Opción B")
    print("C. Opción C")
    print("======================")
    print("Q. Salir")
    print("======================")

    caso = (input("Introduzca una opción: "))

    match caso:
        case "A":
            print("Ha seleccionado la opción A.")           
        case "B":
            print("Ha seleccionado la opción B.")
        case "C":
            print("Ha seleccionado la opción C.")
        case "Q":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no valida.")

