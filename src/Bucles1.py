'''
numero = 1              # Variable de control
while numero <= 5:      # Mientras numero sea menor o igual a 5
    print(numero)       # Mostrar numero en pantalla
    numero += 1         # Numero = Numero + 1

# Modificaciones
# Para mostrar los numeros pares hasta el 100

numero = 0              # Variable de control desde 0
while numero <= 100:    # Mientras numero sea menor o igual a 100
    print(numero)       # Mostrar numero en pantalla
    numero += 2         # Se suma 2 para mostrar pares

# Para mostrar los numeros impares hasta el 100

numero = 0              # Variable de control desde 1
while numero <= 100:    # Mientras numero sea menor o igual a 100
    print(numero)       # Mostrar numero en pantalla
    numero += 2         # Se suma 2 para mostrar pares

# Para mostrar numeros del 5 al 5 desde 100 en orden descendente

numero = 100            # Variable de control desde 100
while numero >= 0:      # Mientras numero sea mayor o igual a 0
    print(numero)       # Mostrar numero en pantalla
    numero -= 5         # Se resta 5 para mostrar de 5 en 5
'''

# Solicitar dos numeros al usuario e imprimir los pares entre ellos

numero1 = int(input("Seleccione el primer numero: "))
numero2 = int(input("Seleccione el segundo numero: "))
if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1
'''
while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1
'''
# Otro metodo

if menor % 2 == 1:
    menor += 1
while menor <= mayor:
    print(menor)
    menor += 2

