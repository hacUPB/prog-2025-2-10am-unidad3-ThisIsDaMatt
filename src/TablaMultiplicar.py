i = 1
numero = int(input("Ingrese el numero del que desea obtener la tabla: "))
print(f"Tabla de multiplicar del {numero}")
while i <= 15:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1