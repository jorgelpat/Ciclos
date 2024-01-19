#Escriba un programa que pida al usuario ingresar la altura 
#y el ancho de un rectángulo y lo dibuje utilizando asteriscos:

alt = int(input("Altura: "))
anch = int(input("Ancho: "))


for i in range(alt):
    for j in range(anch):
        print("*",end=" ")
    print()
