#La entrada del programa debe ser un número entero n
#que indique cuántos términos de la suma se utilizará.

n = int(input('n: '))
sum = 0
for i in range(n):
    sum += (-1)**(i)*(1/(2*i+1))
pi = 4 * sum
print(pi)