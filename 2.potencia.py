#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
number = int(input("Indique un numero: "))
for i in range (number):
    pot = 2**i
    print(f"{pot}",end=" ")

