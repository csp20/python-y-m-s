""" ej 7
Escriba un programa que sume los números ingresados por el usuario mientras el número sea distinto de 
cero.  Cuando la suma sea superior a 100 deje de pedir números y muestre un mensaje con el total.

"""
suma = 0
while True:
    numero = float(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    if suma > 100:
        print("La suma de los números introducidos es superior a 100.")
        break
print("La suma total de los números introducidos es: ", suma)