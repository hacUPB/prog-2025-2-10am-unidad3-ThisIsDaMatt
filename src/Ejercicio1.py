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
if imc < 18.5:
    print("Estás debajo de tu peso ideal.")
else:
    if imc > 18.5 and imc < 24.9:
        print("Estás en un peso normal.")
    else:
        if imc > 25 and imc < 29.9:
            print("Estás en sobre peso.")
        else:
            if imc > 30 and imc < 34.9:
                print("Estás en obesidad leve.")
            else:
                if imc > 35 and imc < 39.9:
                    print("Estás en obesidad moderada.")
                else:
                    if imc > 40:
                        print("Estás en obesidad extrema.")
#Mostrar imc
print("Tu IMC = ", imc)