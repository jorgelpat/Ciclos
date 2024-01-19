#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
number = int(input("Ingrese un numero:\n"))
for i in range(1,11):
    resultado = number * i
    print("{} x {} = {}".format(number,i,resultado))