i = 1
numero = int(input("Ingrese el numero del que desea obtener la tabla: "))
print(f"Tabla de multiplicar del {numero}")
while i <= 15:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1

'''
Solución del profesor:
numero = int(input("Ingrese el numero entero: "))
cont = 1
while cont <= 15:
    res = cont * numero
    print(f"{numero} x {cont} = {res})
    
'''
