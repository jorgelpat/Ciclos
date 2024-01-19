#Desarrolle un programa que entregue un valor aproximado de e, 
#calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

import math
denominador = 2
diferencia = 1
euler = 2
fraccionAnt = 1
fracc = 1
while diferencia > 0.0001:
    fraccionAnt = fracc
    fracc = 1/math.factorial(denominador)
    denominador += 1
    euler += fracc
    diferencia = fraccionAnt-fracc
print(euler) 