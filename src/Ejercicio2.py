#Determina si un numero es par o impar
numero = int(input("Ingrese un numero entero: "))
residuo = numero % 2
#Si residuo es 0, es par
if residuo == 0:
    print(numero, "es par")
else:
#Si no, es impar
    print(numero, "es impar")

