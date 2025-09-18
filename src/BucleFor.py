'''
for cont in range(20): ## Por defecto comienza en 0
    print(cont)

for cont in range(-1, -21, -1): ## Del -1 al -21, en incrementos de -1
    print(cont)

for cont in range(-20, 0, 1): ## Del -20 al 0, en incrementos de 1
    print(cont)
'''
'''
numero = -1
while numero < 0:
    numero = int(input("Ingrese el numero entero: "))
    acum = 0
    for cont in range(1, numero+1):
        if cont % 2 == 0:
            acum += cont
print(f"La suma de los pares es: {acum}")
'''

mensaje = "Universidad Pontificia Bolivariana"
numero = int(input("Ingrese el numero entero positivo: "))
# Imprimir el mensaje un numero de veces
for i in range(numero):
    print(mensaje)