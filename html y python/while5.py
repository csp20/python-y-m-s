""" ej 5
Tenemos una aplicación en la que los usuarios proporcionan números válidos(positivos, negativos o cero).
 Escribir un programa en Python donde un usuario pueda seguir proporcionando los números, y para cada 
 entrada, mostrar por pantalla si es un número positivo, negativo o cero.
El programa terminará cuando el usuario escriba salir. Utilizar una variable opcion 
con valores “ ” o “salir”. Se puede usar break para salir del bucle.
"""
while True:
    opcion = input("Introduce un número o escribe 'salir' para terminar: ")
    if opcion.lower() == 'salir':
        break
    else:
        try:
            numero = float(opcion)
            if numero > 0:
                print("El número es positivo.")
            elif numero < 0:
                print("El número es negativo.")
            else:
                print("El número es cero.")
        except ValueError:
            print("Por favor, introduce un número válido o 'salir'.")