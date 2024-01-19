#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos 
#y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
tramos = 0
truco = False
while truco == False:
    x = int(input("Duracion tramo: "))
    tramos = x + tramos
    if x == 0:
        truco = True
    
if tramos >= 60:
    min = tramos%60
    res = tramos - min
    hora = res/60
    if min > 9:
        print("tiempo total de viaje:   {}:{} horas".format(int(hora),min))
    else:
        print("tiempo total de viaje:   {}:0{} horas".format(int(hora),min))
    
    

    