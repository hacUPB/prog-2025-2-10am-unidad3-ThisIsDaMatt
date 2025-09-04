'''
=====================
Variables de entrada:
=====================
Nombre      |  Tipo
=====================
Opcion      |  String
Temperatura |  Float

=====================
Variables de salida:
=====================
Nombre      |  Tipo
=====================
Conversion  |  Float

=====================
Variable de control:
=====================
Nombre      |  Tipo
=====================
Opcion      |  String
'''

opcion = "L"        # Asigno un valor diferente de Q
while opcion != "Q":
    opcion = input("F. Fahrenheit a Celcius\nC. Celcius a Fehrenheit\nQ. Salir\n")
    opcion = opcion.upper()
    if opcion != "Q":
        temperatura = float(input("Ingrese la temperatura a convertir: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) * (5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C':
                conversion = (temperatura * 9/5) + 32
                print(f"{temperatura}°C = {conversion}°F")
            case 'Q':
                print("Saliendo del programa...")
            case _:
                print("Opción no valida")
    else:
        print("Saliendo del programa...")
        
