#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
#El programa debe mostrar tres columnas que contengan la siguiente información:
#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.

fraccion = 1
i = 1
sum = 0
titulos = ['Potencia', 'Fracción', 'Suma']
for encabezado in titulos:
    print(encabezado, end=" ")
print()
while fraccion > 0.000001:
    fraccion = 1/(2**i)
    sum += fraccion
    print(str(i).ljust(8), end=' ')
    print(str(round(fraccion,4)).ljust(8), end=" ")
    print(round(sum,4))
    i += 1
