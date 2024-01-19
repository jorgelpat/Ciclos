#Escriba un programa que entregue todos los divisores del número entero ingresado:
number = int(input("Ingrese un número: "))
for i in range(1,number+1):
    x = number % i
    if x == 0:
        print(i, end=" ")
