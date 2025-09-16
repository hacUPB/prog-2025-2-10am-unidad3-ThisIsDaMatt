from ModFunciones import *

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("Calcula si un numero es primo.")
                valor = int(input("Ingresa un entero mayor que 1 >> "))
                primo(valor)
            case 2:
                print("Imprime la serie de Fibonacci.")
                num = int(input("Ingresa el numero de terminos >> "))
                fibonacci(num)
            case 3:
                print("Imprime la tabla de multiplicar.")
                num = int(input("Ingresa el numero >> "))
                tabla(num)
            case 4:
                break
            case _:
                print("La opcion que ingreso no es valida.")

if __name__ == "__main__":
    main()

