""" ej4
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) Acumular (ir sumando) en una variable los números ingresados que son pares.
e) Mostrar por pantalla con un mensaje cada uno de los valores anteriormente obtenidos
"""
# Inicializar contadores y acumuladores
num_negativos = 0
num_positivos = 0
num_multiplos_15 = 0
suma_pares = 0

# Pedir al usuario que introduzca 10 valores enteros
for i in range(10):
    num = int(input("Introduce un número entero: "))
    
    # Contar los números negativos
    if num < 0:
        num_negativos += 1
    
    # Contar los números positivos
    elif num > 0:
        num_positivos += 1
    
    # Contar los múltiplos de 15
    if num % 15 == 0:
        num_multiplos_15 += 1
    
    # Acumular los números pares
    if num % 2 == 0:
        suma_pares += num

# Mostrar los resultados
print("Cantidad de valores ingresados negativos:", num_negativos)
print("Cantidad de valores ingresados positivos:", num_positivos)
print("Cantidad de múltiplos de 15:", num_multiplos_15)
print("Suma de los números pares:", suma_pares)