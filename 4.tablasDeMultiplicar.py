#Escriba un programa que muestre una tabla de multiplicar
#Los números deben estar alineados a la derecha.


for i in range(1,11):
    for x in range (1,11):
        mult = str(i * x)
        if x == 10:
            arreglo = mult.rjust(5)
        else:
            arreglo = mult.rjust(4)
        print(arreglo, end=" ")
    print()

#prueba = "probando"
#print(prueba.center(30, "|"))