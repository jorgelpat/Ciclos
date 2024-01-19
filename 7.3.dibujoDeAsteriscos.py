#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:


lado=int(input('Lado: '))
lado2 = lado + 2*(lado-1)
for i in range(lado):
    detalles = ""
    for j in range(lado+2*i):
        detalles += "*"
    print(detalles.center(lado2))
for x in range(1,lado):
    detalles = ""
    for j in range(2,lado+2*(lado-x),1):
        detalles += "*"
    print(detalles.center(lado2))