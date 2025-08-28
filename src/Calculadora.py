control = True

while True:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion = input("Elija una opción: ")
    match opcion:
        case "S":
            print("Suma")
            resultado = num1 + num2
        case "R":
            print("Resta")
            resultado = num1 - num2
        case "M":
            print("Multiplicación")
            resultado = num1 * num2
        case "D":
            print("División")
            try:
                resultado = num1 / num2
            except ZeroDivisionError:
                print("No se puede dividir por cero")
        case "E":
            print("Saliendo de la calculadora.")
            break
        case _:
            print("Modo no valido")
    print(f"Resultado = {resultado}")
        