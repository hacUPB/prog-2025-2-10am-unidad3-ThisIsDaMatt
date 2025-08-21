nombre = input("Ingrese su nombre y apellido: ")
#Opcion 2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso y altura
peso = input("Ingresa tu peso en kilogramos: ")
peso = float(peso)
altura = input("Ingresa tu talla en metros: ")
altura = float(altura)
#Calculos
imc = peso/altura**2
#Mostrar imc
print("Tu IMC = ", imc)
