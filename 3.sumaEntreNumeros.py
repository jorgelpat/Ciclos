#Escriba un programa que pida al usuario dos números enteros, 
#y luego entregue la suma de todos los números que están entre ellos. 
#Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
suma = 0
number1 = int(input("primer numero: "))
number2 = int(input("segundo numero: "))
for i in range(number1+1,number2):
    suma = suma + i
print(f"la suma es {suma}")
