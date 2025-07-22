""" ej 6 
Escriba un programa que lea del teclado un número entero y que compruebe si el número es menor que 10.
 Si lo es, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor 
 correcto (mayor igual  que 10). Finalmente, debe escribir por pantalla el valor leído cuando este 
 sea correcto.
"""
while True:
    numero = int(input("Introduce un número entero mayor o igual a 10: "))
    if numero >= 10:
        print("El número introducido es: ", numero)
        break
    else:
        print("El número es menor que 10. Por favor, introduce un número mayor o igual a 10.")