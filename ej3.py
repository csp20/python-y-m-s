#Solicitar dos números y sumarlos. Evaluar el resultado mostrando los mensajes:
#● Indicar si la suma es par y mayor que 1000
#● Igual que anterior pero menor
#● Indicar si la suma es impar y mayor que 1000
#● Igual que la anterior pero menor
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Sumar los números
suma = numero1 + numero2

# Evaluar condiciones
if suma % 2 == 0 and suma > 1000:
    print("La suma es par y mayor que 1000.")
elif suma % 2 == 0 and suma < 1000:
    print("La suma es par y menor que 1000.")
elif suma % 2 != 0 and suma > 1000:
    print("La suma es impar y mayor que 1000.")
else:
    print("La suma es impar y menor que 1000.")
