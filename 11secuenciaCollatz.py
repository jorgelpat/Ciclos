#La secuencia de Collatz de un número entero se construye de la siguiente forma:

#si el número es par, se lo divide por dos;
#si es impar, se le multiplica tres y se le suma uno;
#la sucesión termina al llegar a uno.

#Programa1
a = int(input("n: "))

while a != 1:
    if a%2 == 0:
        a = int(a/2)
    else:
        a = (a*3)+1
    print(a,end=" ")



    
    


